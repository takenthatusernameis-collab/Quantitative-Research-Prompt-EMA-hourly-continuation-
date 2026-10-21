"""Tests for the pooled robustness legs (scripts/robustness_pooled.py)."""
import gzip

import pandas as pd
import pytest

from scripts.robustness_pooled import (bucket_label, cell_net_totals, drop_top_n_legs,
                                        pool, rank_of, read_trades,
                                        split_subperiods, stability_verdict,
                                        subperiod_stats)


def test_cell_net_totals_recover_win_and_loss_sums():
    """A cell summary implies exact net win and loss totals."""
    summary = {
        'trade_count': 10,
        'net_win_rate': 0.4,
        'net_avg_win': 100.0,
        'net_avg_loss': -50.0,
    }
    win_sum, loss_abs, trades = cell_net_totals(summary)
    assert trades == 10
    assert win_sum == pytest.approx(400.0)
    assert loss_abs == pytest.approx(300.0)


def test_pool_uses_trade_level_totals_not_mean_of_ratios():
    """Pooled PF weights every cell by its own win and loss totals."""
    cells = [
        {'win_sum': 100.0, 'loss_abs': 50.0, 'trades': 2},
        {'win_sum': 900.0, 'loss_abs': 100.0, 'trades': 20},
    ]
    pooled = pool(cells)
    assert pooled['trades'] == 22
    assert pooled['net_profit_factor'] == pytest.approx(1000.0 / 150.0)
    # A mean of the per-cell ratios would be (2.0 + 9.0) / 2 = 5.5
    assert pooled['net_profit_factor'] != pytest.approx(5.5)


def test_pool_handles_no_losses_and_empty_input():
    """A cell set without losses is infinite PF, an empty set is zero."""
    assert pool([{'win_sum': 10.0, 'loss_abs': 0.0, 'trades': 1}])['net_profit_factor'] == float('inf')
    empty = pool([])
    assert empty['trades'] == 0
    assert empty['net_profit_factor'] == 0.0


def test_rank_and_bucket_labels():
    """Ranks come from the descending universe order; buckets follow §2.1.6."""
    order = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
    assert rank_of('ETH/USDT', order) == 2
    assert rank_of('NOPE/USDT', order) == len(order) + 1
    assert bucket_label(1) == '1-10'
    assert bucket_label(10) == '1-10'
    assert bucket_label(11) == '11-50'
    assert bucket_label(200) == '101-200'
    assert bucket_label(266) == '201+'


def test_drop_top_n_removes_the_largest_names():
    """Dropping the N largest market caps removes exactly those symbols."""
    order = ['A/USDT', 'B/USDT', 'C/USDT']
    cells = [
        {'symbol': 'A/USDT', 'win_sum': 100.0, 'loss_abs': 10.0, 'trades': 1},
        {'symbol': 'B/USDT', 'win_sum': 50.0, 'loss_abs': 10.0, 'trades': 1},
        {'symbol': 'C/USDT', 'win_sum': 25.0, 'loss_abs': 10.0, 'trades': 1},
    ]
    legs = drop_top_n_legs(cells, order, [1, 2])
    assert legs[0]['dropped_n'] == 1
    assert legs[0]['trades'] == 2
    assert legs[0]['net_profit_factor'] == pytest.approx(75.0 / 20.0)
    assert legs[1]['dropped_n'] == 2
    assert legs[1]['trades'] == 1


def test_split_subperiods_assigns_chronological_slices():
    """Trades are spread over the cell's own timeline in equal-time slices."""
    times = pd.to_datetime(
        ['2024-01-01 00:00:00+00:00', '2024-01-02 00:00:00+00:00',
         '2024-01-03 00:00:00+00:00', '2024-01-04 00:00:00+00:00'], utc=True)
    buckets = split_subperiods(times, 2)
    assert list(buckets) == [0, 0, 1, 1]


def test_subperiod_stats_and_verdicts():
    """Subperiod PFs are computed per slice and drive the stability verdict."""
    pnl = pd.Series([100.0, -50.0, 200.0, -300.0, -100.0, -20.0])
    buckets = [0, 0, 1, 1, 2, 2]
    stats = subperiod_stats(pnl, buckets, 3)
    assert [s['trades'] for s in stats] == [2, 2, 2]
    assert stats[0]['net_profit_factor'] == pytest.approx(100.0 / 50.0)
    assert stats[1]['net_profit_factor'] == pytest.approx(200.0 / 300.0)
    assert stats[2]['net_profit_factor'] == pytest.approx(0.0)
    # every slice holds fewer trades than the evaluation floor -> thin slices
    assert [s['class'] for s in stats] == ['thin_win', 'thin_loss', 'thin_loss']


def test_stability_verdict_treats_a_losing_sliced_as_fragile():
    """A slice that lost money blocks a 'stable' verdict even when it is thin."""
    subperiods = [
        {'trades': 12, 'net_profit_factor': 2.7, 'class': 'win'},
        {'trades': 3, 'net_profit_factor': 0.0, 'class': 'thin_loss'},
        {'trades': 6, 'net_profit_factor': 1.03, 'class': 'win'},
    ]
    assert stability_verdict(subperiods) == 'fragile'


def test_stability_verdict_stable_and_loss_only():
    """All slices positive -> stable, no positive slice -> loss_only."""
    stable = [
        {'trades': 10, 'net_profit_factor': 1.2, 'class': 'win'},
        {'trades': 10, 'net_profit_factor': 1.1, 'class': 'win'},
    ]
    assert stability_verdict(stable) == 'stable'
    loss_only = [
        {'trades': 10, 'net_profit_factor': 0.8, 'class': 'loss'},
        {'trades': 10, 'net_profit_factor': 0.4, 'class': 'loss'},
    ]
    assert stability_verdict(loss_only) == 'loss_only'
    thin = [
        {'trades': 2, 'net_profit_factor': 1.2, 'class': 'thin_win'},
        {'trades': 1, 'net_profit_factor': 1.1, 'class': 'thin_win'},
    ]
    assert stability_verdict(thin) == 'insufficient'
    assert stability_verdict([{'trades': 0, 'net_profit_factor': None, 'class': 'empty'}]) \
        == 'no_trades'


def test_read_trades_handles_both_blotter_layouts(tmp_path):
    """The run mixes the gzip and the legacy layout; both must be readable.

    The five largest market-cap names still carry the legacy uncompressed
    `trades.csv`, the rest carry `trades.csv.gz`. A reader that only knows
    the gzip layout skips - or crashes on - the top of the universe.
    """
    columns = ['symbol', 'entry_time', 'pnl_net']
    gz_dir = tmp_path / 'P50_100'
    gz_dir.mkdir()
    with gzip.open(gz_dir / 'trades.csv.gz', 'wt', encoding='utf-8') as fh:
        fh.write('symbol,entry_time,pnl_net\nBTC/USDT,2024-01-01 00:00:00+00:00,1.5\n')
    legacy_dir = tmp_path / 'legacy'
    legacy_dir.mkdir()
    (legacy_dir / 'trades.csv').write_text(
        'symbol,entry_time,pnl_net\nBTC/USDT,2024-01-01 00:00:00+00:00,2.5\n')

    gz = read_trades(gz_dir)
    legacy = read_trades(legacy_dir)

    assert len(gz) == 1 and len(legacy) == 1
    assert gz['pnl_net'].iloc[0] == pytest.approx(1.5)
    assert legacy['pnl_net'].iloc[0] == pytest.approx(2.5)
    assert str(gz['entry_time'].dtype) == str(legacy['entry_time'].dtype)
