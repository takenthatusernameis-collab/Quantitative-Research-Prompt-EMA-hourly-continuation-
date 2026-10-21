"""Tests for the grid refresh audit (scripts/refresh_audit.py)."""
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts.refresh_audit import (compare_cells, fixture_bar_sequence,
                                   read_cell, symbol_bar_sequence, write_report)

METRICS = ('trade_count', 'net_profit_factor', 'gross_profit_factor',
           'sharpe_ratio', 'max_drawdown', 'net_win_rate')


def _write_cell(run_dir: Path, symbol: str, fast: int, slow: int, metrics: dict,
                timestamps: list) -> None:
    cell = run_dir / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    cell.mkdir(parents=True, exist_ok=True)
    summary = {'symbol': symbol, 'P_fast': fast, 'P_slow': slow}
    summary.update(metrics)
    (cell / 'summary.json').write_text(json.dumps(summary))
    pd.DataFrame({'timestamp': timestamps, 'equity': [1.0] * len(timestamps),
                  'index': range(len(timestamps))}).to_csv(cell / 'equity.csv.gz',
                                                            index=False)


def test_read_cell_returns_the_reported_metrics(tmp_path):
    """The audit compares the metrics the cell reports."""
    run_dir = tmp_path / 'grid'
    _write_cell(run_dir, 'AAA/USDT', 8, 12,
                {'trade_count': 10, 'net_profit_factor': 0.9, 'gross_profit_factor': 1.0,
                 'sharpe_ratio': -0.2, 'max_drawdown': 0.3, 'net_win_rate': 0.4},
                ['2024-01-01 00:00:00+00:00'])
    metrics = read_cell(run_dir, 'AAA/USDT', 8, 12)
    assert metrics['trade_count'] == 10
    assert metrics['net_profit_factor'] == 0.9
    assert set(metrics) == set(METRICS)


def test_symbol_bar_sequence_reads_the_equity_artifact(tmp_path):
    """The bar sequence the grid ran on is the equity artifact's timestamps."""
    run_dir = tmp_path / 'grid'
    stamps = ['2024-01-01 00:00:00+00:00', '2024-01-01 01:00:00+00:00']
    _write_cell(run_dir, 'AAA/USDT', 8, 12, {}, stamps)
    assert symbol_bar_sequence(run_dir, 'AAA/USDT') == stamps


def test_fixture_bar_sequence_reads_the_fixture(tmp_path):
    """The bar sequence on disk is the fixture's timestamps."""
    fixtures = tmp_path / 'fixtures'
    fixtures.mkdir()
    stamps = ['2024-01-01 00:00:00+00:00']
    pd.DataFrame({'timestamp': stamps, 'close': [1.0]}).to_csv(
        fixtures / 'AAA_USDT.csv', index=False)
    assert fixture_bar_sequence(str(fixtures), 'AAA/USDT') == stamps


def test_compare_cells_flags_a_cell_that_crossed_pf_one():
    """A drift that only moves the third decimal is a footnote; crossing a
    threshold is a finding, and the audit must say which it is."""
    before = {'AAA/USDT/P8_12': {'net_profit_factor': 1.02, 'trade_count': 10},
              'AAA/USDT/P8_20': {'net_profit_factor': 0.98, 'trade_count': 10}}
    after = {'AAA/USDT/P8_12': {'net_profit_factor': 0.99, 'trade_count': 9},
             'AAA/USDT/P8_20': {'net_profit_factor': 0.980001, 'trade_count': 10}}
    result = compare_cells(before, after)
    assert result['n_cells'] == 2
    assert result['n_changed'] == 2
    assert result['n_crossed_pf_1'] == 1
    assert result['max_abs_net_pf_delta'] == pytest.approx(0.03)
    crossed = [r for r in result['rows'] if r['crossed_pf_1']]
    assert crossed[0]['cell'] == 'AAA/USDT/P8_12'


def test_write_report_writes_a_readable_report(tmp_path):
    """The report is the artifact a reader actually reads."""
    payload = {
        'generated_at': '2026-10-21T00:00:00+00:00',
        'source_run': 'results/x_grid',
        'reason': 'fixture re-fetch',
        'symbols': [{'symbol': 'AAA/USDT', 'bars_before': 10, 'bars_now': 11,
                     'first_before': 'a', 'first_now': 'b', 'last_before': 'c',
                     'last_now': 'd', 'identical': False}],
        'comparison': compare_cells(
            {'AAA/USDT/P8_12': {'net_profit_factor': 1.0, 'trade_count': 3}},
            {'AAA/USDT/P8_12': {'net_profit_factor': 1.0, 'trade_count': 3}}),
        'reading': 'The refresh moves the cells by the amount shown above.',
    }
    out_dir = tmp_path / 'audit'
    out_dir.mkdir()
    write_report(out_dir, payload)
    text = (out_dir / 'summary.md').read_text()
    assert 'AAA/USDT' in text
    assert 'Cells re-run | 1' in text
    assert 'The refresh moves the cells' in text
