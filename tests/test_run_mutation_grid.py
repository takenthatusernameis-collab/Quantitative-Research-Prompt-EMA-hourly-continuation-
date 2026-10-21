"""Tests for the parallel mutation-grid runner."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from scripts.run_grid import CONFIG_DEFAULTS, period_pairs, run_cell, symbol_dir_name
from scripts.run_mutation_grid import (cell_dir_for, run_symbol, scan_completed,
                                       write_progress)

PAIRS = period_pairs()


def write_fixture(path: Path, n_bars: int = 900) -> None:
    """A synthetic hourly series with enough bars for the slowest EMA."""
    rng = np.random.default_rng(7)
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


def test_run_symbol_writes_one_artifact_set_per_cell(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    run_dir = tmp_path / 'run'
    job = {'results_dir': str(run_dir), 'symbol': 'TEST/USDT',
           'fixture_base': str(fixture_base), 'config': dict(CONFIG_DEFAULTS)}
    result = run_symbol(job)
    assert result['errors'] == []
    assert len(result['cells']) == len(PAIRS)
    for fast, slow in PAIRS:
        cdir = cell_dir_for(run_dir, 'TEST/USDT', fast, slow)
        assert (cdir / 'config.json').exists()
        assert (cdir / 'summary.json').exists()
        assert (cdir / 'summary.md').exists()
        assert (cdir / 'trades.csv.gz').exists()


def test_run_symbol_reproduces_the_serial_runner(tmp_path):
    """The mutation runner has to be the baseline engine, not a copy of it.

    A cell written by `scripts/run_mutation_grid.py` has to match the cell
    `scripts.run_grid.run_cell` produces with the same config, cell by cell.
    """
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    run_dir = tmp_path / 'run'
    job = {'results_dir': str(run_dir), 'symbol': 'TEST/USDT',
           'fixture_base': str(fixture_base), 'config': dict(CONFIG_DEFAULTS)}
    run_symbol(job)
    from data.data_loader import load_ohlcv_csv
    df = load_ohlcv_csv(str(fixture_base / 'TEST_USDT.csv'))
    for fast, slow in PAIRS[:3]:
        _, _, metrics = run_cell(
            'TEST/USDT', df, fast, slow, CONFIG_DEFAULTS['taker_fee_bps'],
            CONFIG_DEFAULTS['slippage_bps'], CONFIG_DEFAULTS['rr'],
            CONFIG_DEFAULTS['stricter_trend'], CONFIG_DEFAULTS['min_risk_atr'],
            CONFIG_DEFAULTS['atr_threshold'], CONFIG_DEFAULTS['conservative_exit'],
            oos_fraction=None, sizing=CONFIG_DEFAULTS['sizing'],
            risk_fraction=CONFIG_DEFAULTS['risk_fraction'],
            max_notional_multiple=CONFIG_DEFAULTS['max_notional_multiple'])
        stored = json.loads(
            (cell_dir_for(run_dir, 'TEST/USDT', fast, slow) / 'summary.json').read_text())
        for key in ('trade_count', 'net_profit_factor', 'gross_profit_factor',
                    'sharpe_ratio', 'max_drawdown'):
            assert stored[key] == pytest.approx(metrics[key], rel=1e-12, abs=1e-12)


def test_run_symbol_skips_cells_that_are_already_on_disk(tmp_path):
    """A finished cell is never re-run: the run has to be resumable."""
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    run_dir = tmp_path / 'run'
    job = {'results_dir': str(run_dir), 'symbol': 'TEST/USDT',
           'fixture_base': str(fixture_base), 'config': dict(CONFIG_DEFAULTS)}
    first = run_symbol(job)
    assert len(first['cells']) == len(PAIRS)
    # Mark one cell as finished long ago; the second pass must keep it.
    cdir = cell_dir_for(run_dir, 'TEST/USDT', *PAIRS[0])
    stamp = cdir / 'summary.json'
    stamp.write_text(stamp.read_text() + ' ')
    second = run_symbol(job)
    assert len(second['cells']) == len(PAIRS)
    assert (cdir / 'summary.json').read_text().endswith(' ')


def test_scan_completed_finds_the_cells_on_disk(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    run_dir = tmp_path / 'run'
    job = {'results_dir': str(run_dir), 'symbol': 'TEST/USDT',
           'fixture_base': str(fixture_base), 'config': dict(CONFIG_DEFAULTS)}
    run_symbol(job)
    completed = scan_completed(run_dir, ['TEST/USDT'])
    assert completed == {('TEST/USDT', f, s) for f, s in PAIRS}
    assert scan_completed(run_dir, ['OTHER/USDT']) == set()


def test_write_progress_is_self_consistent(tmp_path):
    run_dir = tmp_path / 'run'
    run_dir.mkdir()
    symbols = ['A/USDT', 'B/USDT']
    completed = {('A/USDT', f, s) for f, s in PAIRS}
    progress = write_progress(run_dir, 'test_run', '20260101_000000', symbols,
                               completed, len(PAIRS))
    assert progress['n_symbols'] == len(symbols)
    assert progress['completed_cells'] == len(completed)
    assert len(progress['completed']) == len(completed)
    assert progress['next_cell'] == ['B/USDT', PAIRS[0][0], PAIRS[0][1]]
    assert progress['all_symbols_processed'] is False
    full = set(completed) | {('B/USDT', f, s) for f, s in PAIRS}
    progress = write_progress(run_dir, 'test_run', '20260101_000000', symbols,
                               full, len(PAIRS))
    assert progress['next_cell'] is None
    assert progress['all_symbols_processed'] is True
    assert progress['n_symbols'] * progress['n_pairs'] == progress['completed_cells']


def test_shipped_mutation_grid_keeps_the_baseline_config(tmp_path):
    """The ATR mutation may only change the registered mutation keys."""
    parent = Path('results/20261019_135940_grid/run_config.json')
    child = Path('results/20261021_172619_grid/run_config.json')
    if not parent.exists() or not child.exists():
        pytest.skip('mutation run not present')
    parent_cfg = json.loads(parent.read_text())['config']
    child_cfg = json.loads(child.read_text())['config']
    changed = {k for k in set(parent_cfg) | set(child_cfg)
               if parent_cfg.get(k) != child_cfg.get(k)}
    assert changed <= {'min_risk_atr', 'atr_threshold'}
    assert 'min_risk_atr' in changed
    assert child_cfg['min_risk_atr'] is True
    assert parent_cfg['min_risk_atr'] is False
