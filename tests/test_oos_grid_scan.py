"""Tests for the grid-wide out-of-sample audit (scripts/oos_grid_scan.py)."""
import gzip
import json

import pandas as pd
import pytest

from scripts.oos_grid_scan import (compare_with_candidate_check, entry_start_index,
                                    net_profit_factor, parse_cells, read_trades,
                                    screen_cell, screen_survivors, stressed_pnl_net,
                                    verdict)


def _trades(entries):
    """Build a trade blotter with the columns the screen reads."""
    return pd.DataFrame({
        'bar_index': [e[0] for e in entries],
        'pnl': [e[1] for e in entries],
        'pnl_net': [e[2] for e in entries],
        'entry_cost': [e[3] for e in entries],
        'exit_cost': [e[4] for e in entries],
    })


def test_entry_start_index_mirrors_the_grid_runner():
    """The OOS window opens at the same bar the grid runner would use."""
    assert entry_start_index(22000, 0.35) == 14300
    assert entry_start_index(22000, 0.5) == 11000
    # The same float expression the grid runner uses, so the boundary matches
    # bit for bit (22000 * 0.35 is 7699.999... in binary floating point).
    assert entry_start_index(22000, 0.65) == 7699
    # A non-OOS run keeps every bar.
    assert entry_start_index(22000, None) == 0
    assert entry_start_index(22000, 0.0) == 0
    assert entry_start_index(22000, 1.0) == 0


def test_net_profit_factor_uses_trade_level_wins_over_losses():
    """PF is the sum of wins over the sum of losses, not a mean of ratios."""
    assert net_profit_factor([100.0, -50.0, 200.0, -300.0]) == pytest.approx(300.0 / 350.0)
    # No trades is missing evidence, not evidence of a loss.
    assert net_profit_factor([]) is None
    # No losses at all is an infinite PF.
    assert net_profit_factor([1.0, 2.0]) == float('inf')
    assert net_profit_factor([-1.0, -2.0]) == 0.0


def test_stressed_pnl_net_charges_the_extra_cost_once_per_side():
    """Doubling the costs subtracts one more entry_cost + exit_cost per trade."""
    pnl_net = [90.0, -100.0]
    entry_cost = [5.0, 6.0]
    exit_cost = [5.0, 4.0]
    out = stressed_pnl_net(pnl_net, entry_cost, exit_cost, 2.0)
    assert list(out) == [80.0, -110.0]
    # A multiplier of 1 leaves the trade untouched.
    assert list(stressed_pnl_net(pnl_net, entry_cost, exit_cost, 1.0)) == [90.0, -100.0]
    assert list(stressed_pnl_net([], [], [], 2.0)) == []


def test_screen_cell_splits_trades_at_the_oos_boundary():
    """Only trades entered on or after the boundary belong to the OOS window."""
    trades = _trades([
        (10, 100.0, 90.0, 5.0, 5.0),
        (99, -200.0, -210.0, 4.0, 6.0),
        (100, 300.0, 288.0, 6.0, 6.0),
    ])
    stats = screen_cell(trades, entry_start=100, stress_multiplier=2.0)
    assert stats['trades'] == 3
    assert stats['oos_trades'] == 1
    assert stats['oos_net_pf'] == pytest.approx(float('inf'))
    assert stats['oos_stress_net_pf'] == pytest.approx(float('inf'))
    assert stats['oos_net_pnl'] == pytest.approx(288.0)
    # The stressed OOS P&L subtracts the extra cost of the trade.
    assert stats['oos_stress_net_pnl'] == pytest.approx(288.0 - 12.0)
    # The full-sample figures cover every trade.
    assert stats['net_pf'] == pytest.approx(378.0 / 210.0)
    assert stats['stress_net_pf'] == pytest.approx(356.0 / 220.0)


def test_screen_cell_without_oos_trades_reports_no_evidence():
    """A cell with no trade in the window has no OOS profit factor."""
    trades = _trades([(1, 100.0, 90.0, 5.0, 5.0)])
    stats = screen_cell(trades, entry_start=100)
    assert stats['oos_trades'] == 0
    assert stats['oos_net_pf'] is None
    assert stats['oos_net_pnl'] == 0.0


def test_screen_survivors_keeps_only_tradeable_positive_cells():
    """The loose screen keeps cells with enough OOS trades and a positive PF."""
    rows = [
        {'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_trades': 100, 'oos_net_pf': 1.4},
        {'symbol': 'B/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_trades': 100, 'oos_net_pf': 0.95},
        {'symbol': 'C/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_trades': 100, 'oos_net_pf': 0.85},
        {'symbol': 'D/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_trades': 5, 'oos_net_pf': 2.0},
    ]
    survivors = screen_survivors(rows, screen_pf=0.9, min_trades=30)
    assert [r['symbol'] for r in survivors] == ['A/USDT', 'B/USDT']


def test_verdict_applies_the_full_section_3_4_gate():
    """A cell needs OOS PF, OOS Sharpe, trade count and both cost-stress legs."""
    oos = {'trade_count': 40, 'net_profit_factor': 1.2, 'sharpe_ratio': 0.5}
    stress_oos = {'trade_count': 40, 'net_profit_factor': 1.1, 'sharpe_ratio': 0.4}
    assert verdict(oos, stress_oos, full_stress_pf=1.05, min_trades=30) == 'credible candidate'
    # The full-sample stress leg failing demotes the cell to exploratory.
    assert verdict(oos, stress_oos, full_stress_pf=0.9, min_trades=30) == 'exploratory signal'
    # The stressed OOS leg failing does the same.
    assert verdict(oos, {'trade_count': 40, 'net_profit_factor': 0.9, 'sharpe_ratio': 0.1},
                   full_stress_pf=1.05, min_trades=30) == 'exploratory signal'
    # Too few OOS trades is an outright reject.
    thin = {'trade_count': 10, 'net_profit_factor': 1.2, 'sharpe_ratio': 0.5}
    assert verdict(thin, stress_oos, full_stress_pf=1.05, min_trades=30) == 'rejected'
    # A negative OOS Sharpe blocks promotion.
    assert verdict({'trade_count': 40, 'net_profit_factor': 1.2, 'sharpe_ratio': -0.1},
                   stress_oos, full_stress_pf=1.05, min_trades=30) == 'exploratory signal'


def test_parse_cells_reads_the_symbol_fast_slow_list():
    """The cell list uses the same "SYMBOL/USDT:fast:slow" syntax as the pipeline."""
    assert parse_cells('JASMY/USDT:20:200,BABYDOGE/USDT:50:89') == [
        ('JASMY/USDT', 20, 200), ('BABYDOGE/USDT', 50, 89)]


def test_read_trades_handles_both_artifact_layouts(tmp_path):
    """The gzip layout and the legacy uncompressed layout both read."""
    blotter = _trades([(1, 100.0, 90.0, 5.0, 5.0)])
    legacy_dir = tmp_path / 'legacy'
    legacy_dir.mkdir()
    blotter.to_csv(legacy_dir / 'trades.csv', index=False)
    gz_dir = tmp_path / 'gzip'
    gz_dir.mkdir()
    with gzip.open(gz_dir / 'trades.csv.gz', 'wt') as fh:
        blotter.to_csv(fh, index=False)

    legacy = read_trades(legacy_dir)
    gzipped = read_trades(gz_dir)
    assert list(legacy.columns) == list(gzipped.columns)
    assert legacy['pnl_net'].tolist() == gzipped['pnl_net'].tolist() == [90.0]


def test_compare_with_candidate_check_measures_the_screen_error(tmp_path):
    """The screen fidelity is measured against the exact candidate-check numbers."""
    (tmp_path / 'summary.json').write_text(json.dumps({'cells': [
        {'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 12,
         'legs': {'oos': {'net_profit_factor': 1.25, 'trade_count': 40}}},
        {'symbol': 'B/USDT', 'P_fast': 8, 'P_slow': 12,
         'legs': {'oos': {'net_profit_factor': 0.5, 'trade_count': 10}}},
    ]}))
    rows = [
        {'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_net_pf': 1.20, 'oos_trades': 38},
        {'symbol': 'B/USDT', 'P_fast': 8, 'P_slow': 12, 'oos_net_pf': 0.40, 'oos_trades': 9},
    ]
    fidelity = compare_with_candidate_check(rows, tmp_path)
    assert fidelity['available'] is True
    assert fidelity['n_compared'] == 2
    assert fidelity['max_abs_pf_delta'] == pytest.approx(0.10)
    assert fidelity['max_abs_trade_delta'] == 2
    # Both put the net PF on the same side of 1.0.
    assert fidelity['sign_agreement'] == 2
