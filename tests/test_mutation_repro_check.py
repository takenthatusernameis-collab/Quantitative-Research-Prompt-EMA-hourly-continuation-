"""Tests for the reproduction check of a mutation child grid."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from scripts.mutation_repro_check import (cell_dir, compare_metrics,
                                           compare_trades, complete_child_symbols,
                                           path_difference, read_blotter,
                                           reproduce_cell, sample_cells)
from scripts.run_grid import CONFIG_DEFAULTS, period_pairs, run_cell, symbol_dir_name

PAIRS = period_pairs()


def write_fixture(path: Path, n_bars: int = 900) -> None:
    rng = np.random.default_rng(23)
    close = 100.0 + np.cumsum(rng.normal(0.0, 0.4, n_bars))
    df = pd.DataFrame({
        'timestamp': pd.date_range('2023-01-01', periods=n_bars, freq='h'),
        'open': close,
        'high': close + 0.2,
        'low': close - 0.2,
        'close': close,
        'volume': 100.0 + rng.random(n_bars),
    })
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_run(run_dir: Path, fixture_base: Path, symbol: str, config: dict) -> None:
    """Write the full grid of one symbol with the given config."""
    from data.data_loader import load_ohlcv_csv
    from scripts.run_grid import save_cell
    df = load_ohlcv_csv(str(fixture_base / f'{symbol_dir_name(symbol)}.csv'))
    for fast, slow in PAIRS:
        trades, equity_df, metrics = run_cell(
            symbol, df, fast, slow, config['taker_fee_bps'], config['slippage_bps'],
            config['rr'], config['stricter_trend'], config['min_risk_atr'],
            config['atr_threshold'], config['conservative_exit'], oos_fraction=None,
            sizing=config['sizing'], risk_fraction=config['risk_fraction'],
            max_notional_multiple=config['max_notional_multiple'])
        save_cell(run_dir, symbol, fast, slow, trades, equity_df, metrics, config)


def test_a_rerun_reproduces_the_stored_artifacts(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    cfg = dict(CONFIG_DEFAULTS)
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', cfg)

    fast, slow = PAIRS[0]
    result = reproduce_cell(run_dir, 'TEST/USDT', fast, slow, cfg,
                            str(fixture_base))
    assert result['reproduced'] is True
    assert result['trade_diffs'] == []
    assert result['max_abs_metric_delta'] == 0.0


def test_a_tampered_summary_is_not_reproduced(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    cfg = dict(CONFIG_DEFAULTS)
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', cfg)

    fast, slow = PAIRS[0]
    summary_path = cell_dir(run_dir, 'TEST/USDT', fast, slow) / 'summary.json'
    summary = json.loads(summary_path.read_text())
    summary['net_profit_factor'] = 1.2345
    summary_path.write_text(json.dumps(summary))

    result = reproduce_cell(run_dir, 'TEST/USDT', fast, slow, cfg,
                            str(fixture_base))
    assert result['reproduced'] is False
    assert result['metric_deltas']['net_profit_factor'] > 0


def test_a_tampered_blotter_is_not_reproduced(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    cfg = dict(CONFIG_DEFAULTS)
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', cfg)

    fast, slow = PAIRS[0]
    cdir = cell_dir(run_dir, 'TEST/USDT', fast, slow)
    blotter = read_blotter(cdir)
    if len(blotter):
        blotter.loc[0, 'qty'] = float(blotter.loc[0, 'qty']) * 1.5
        blotter.to_csv(cdir / 'trades.csv.gz', index=False, compression='gzip')
        result = reproduce_cell(run_dir, 'TEST/USDT', fast, slow, cfg,
                                str(fixture_base))
        assert result['reproduced'] is False
        assert result['trade_diffs']


def test_the_mutation_changes_the_path_and_not_only_the_trade_list(tmp_path):
    """The ATR filter re-times the entries, it does not prune the parent."""
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    parent_cfg = dict(CONFIG_DEFAULTS)
    child_cfg = dict(CONFIG_DEFAULTS)
    child_cfg['min_risk_atr'] = True
    parent_dir = tmp_path / 'parent'
    child_dir = tmp_path / 'child'
    build_run(parent_dir, fixture_base, 'TEST/USDT', parent_cfg)
    build_run(child_dir, fixture_base, 'TEST/USDT', child_cfg)

    fast, slow = PAIRS[0]
    path = path_difference(cell_dir(parent_dir, 'TEST/USDT', fast, slow),
                           cell_dir(child_dir, 'TEST/USDT', fast, slow))
    assert path['child_trades'] < path['parent_trades']
    assert path['parent_only_entry_bars'] > 0
    assert path['first_divergent_bar'] is not None


def test_complete_child_symbols_needs_a_full_grid(tmp_path):
    run_dir = tmp_path / 'run'
    (run_dir / 'results' / 'A_USDT' / f'P{PAIRS[0][0]}_{PAIRS[0][1]}').mkdir(parents=True)
    assert complete_child_symbols(run_dir, ['A/USDT', 'B/USDT']) == []


def test_sample_cells_spreads_over_the_symbols():
    symbols = [f'S{index}/USDT' for index in range(20)]
    picks = sample_cells(symbols, 5)
    assert len(picks) == 5
    assert len({symbol for symbol, _, _ in picks}) == 5
    assert sample_cells([], 5) == []


def test_compare_trades_reports_a_different_trade_count():
    stored = pd.DataFrame([{'bar_index': 1, 'pnl': 1.0}])
    rerun = pd.DataFrame([{'bar_index': 1, 'pnl': 1.0}, {'bar_index': 2, 'pnl': 2.0}])
    assert compare_trades(stored, rerun) == ['trade_count 2 != 1']


def test_compare_metrics_treats_a_missing_field_as_a_mismatch():
    # a field that is missing on both sides is not a difference
    deltas = compare_metrics({'trade_count': 3}, {'trade_count': 3})
    assert deltas['trade_count'] == 0.0
    assert deltas['net_profit_factor'] == 0.0
    # a field that is missing on one side only is a mismatch
    deltas = compare_metrics({'trade_count': 3, 'net_profit_factor': 1.0},
                              {'trade_count': 3})
    assert deltas['net_profit_factor'] == float('inf')
