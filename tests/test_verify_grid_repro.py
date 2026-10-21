"""Tests for the grid reproducibility check (scripts/verify_grid_repro.py)."""
import json
from pathlib import Path

import pytest

from scripts.verify_grid_repro import check_cell, grid_cells, write_report


def _write_cell(run_dir: Path, symbol: str, fast: int, slow: int, metrics: dict) -> None:
    cell = run_dir / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    cell.mkdir(parents=True, exist_ok=True)
    summary = {'symbol': symbol, 'P_fast': fast, 'P_slow': slow}
    summary.update(metrics)
    (cell / 'summary.json').write_text(json.dumps(summary))


def test_grid_cells_reads_every_cell_of_the_run(tmp_path):
    """The check must see the blocked cells as well, to skip them."""
    run_dir = tmp_path / 'grid'
    _write_cell(run_dir, 'AAA/USDT', 8, 12, {'trade_count': 1})
    _write_cell(run_dir, 'AAA/USDT', 8, 20, {'trade_count': 2})
    blocked = run_dir / 'results' / 'AAA_USDT' / 'P8_26'
    blocked.mkdir(parents=True)
    (blocked / 'summary.json').write_text(json.dumps(
        {'symbol': 'AAA/USDT', 'P_fast': 8, 'P_slow': 26, 'blocked': True}))
    cells = grid_cells(run_dir)
    assert sorted(cells) == [('AAA/USDT', 8, 12), ('AAA/USDT', 8, 20)]


def test_check_cell_reports_a_cell_that_reproduces(tmp_path):
    """A cell whose fixture is unchanged reproduces exactly."""
    import pandas as pd
    from scripts.run_grid import CONFIG_DEFAULTS, run_cell
    from data.data_loader import load_ohlcv_csv

    fixtures = tmp_path / 'fixtures'
    fixtures.mkdir()
    n = 800
    close = [100.0 + (i % 17) * 0.3 for i in range(n)]
    pd.DataFrame({
        'timestamp': pd.date_range('2024-01-01', periods=n, freq='h'),
        'open': close, 'high': [c + 0.5 for c in close],
        'low': [c - 0.5 for c in close], 'close': close, 'volume': 1000.0,
    }).to_csv(fixtures / 'AAA_USDT.csv', index=False)

    df = load_ohlcv_csv(str(fixtures / 'AAA_USDT.csv'))
    _, _, metrics = run_cell(
        'AAA/USDT', df, 8, 12, CONFIG_DEFAULTS['taker_fee_bps'],
        CONFIG_DEFAULTS['slippage_bps'], CONFIG_DEFAULTS['rr'],
        CONFIG_DEFAULTS['stricter_trend'], CONFIG_DEFAULTS['min_risk_atr'],
        CONFIG_DEFAULTS['atr_threshold'], True, oos_fraction=None,
        sizing=CONFIG_DEFAULTS['sizing'],
        risk_fraction=CONFIG_DEFAULTS['risk_fraction'],
        max_notional_multiple=CONFIG_DEFAULTS['max_notional_multiple'])

    run_dir = tmp_path / 'grid'
    _write_cell(run_dir, 'AAA/USDT', 8, 12, {
        'trade_count': metrics.get('trade_count'),
        'net_profit_factor': metrics.get('net_profit_factor'),
        'sharpe_ratio': metrics.get('sharpe_ratio'),
    })
    row = check_cell((str(run_dir), 'AAA/USDT', 8, 12, str(fixtures), 'reference'))
    assert row['reproduces'] is True
    # The fast engine has to reproduce the same cell.
    fast_row = check_cell((str(run_dir), 'AAA/USDT', 8, 12, str(fixtures), 'fast'))
    assert fast_row['reproduces'] is True
    assert fast_row['trade_count_after'] == row['trade_count_after']


def test_write_report_names_the_stale_cells(tmp_path):
    """A stale cell is the thing the report has to make visible."""
    payload = {
        'generated_at': '2026-10-21T00:00:00+00:00',
        'source_run': 'results/x_grid',
        'fixture_base': 'data/fixtures',
        'n_cells': 2,
        'n_reproducing': 1,
        'n_stale': 1,
        'stale': [{'symbol': 'AAA/USDT', 'P_fast': 8, 'P_slow': 12,
                   'trade_count_before': 10, 'trade_count_after': 9,
                   'net_pf_before': 0.5, 'net_pf_after': 0.49}],
    }
    out_dir = tmp_path / 'repro'
    out_dir.mkdir()
    write_report(out_dir, payload)
    text = (out_dir / 'summary.md').read_text()
    assert 'AAA/USDT' in text
    assert 'Cells that do NOT reproduce | 1' in text
    assert 'refresh_audit.py' in text
