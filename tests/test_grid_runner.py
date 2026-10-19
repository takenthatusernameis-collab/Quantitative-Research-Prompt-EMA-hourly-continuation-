"""Tests for the full EMA grid runner and grid aggregation."""
import itertools
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts.run_grid import GRID_PAIRS, PERIOD_GRID, period_pairs, symbol_dir_name
from scripts.aggregate_grid import label_cell, load_cells, per_pair_table, per_symbol_table


def test_period_grid_matches_prompt_spec():
    """PROMPT.md §1.1 registers exactly these periods."""
    assert PERIOD_GRID == [8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200]


def test_grid_pairs_are_all_valid_combinations():
    """Every registered pair has P_fast < P_slow, and the count matches C(n,2)."""
    pairs = period_pairs()
    assert len(pairs) == len(list(itertools.combinations(PERIOD_GRID, 2))) == 66
    for fast, slow in pairs:
        assert fast < slow
        assert fast in PERIOD_GRID and slow in PERIOD_GRID
    # No duplicates and pairs are unique.
    assert len(set(pairs)) == len(pairs)


def test_grid_pairs_cover_every_unordered_combination():
    """The grid must not silently omit a combination."""
    assert set(GRID_PAIRS) == set(itertools.combinations(PERIOD_GRID, 2))


def test_symbol_dir_name_is_filesystem_safe():
    assert symbol_dir_name('BTC/USDT') == 'BTC_USDT'
    assert '/' not in symbol_dir_name('ETH/USDT')


def _write_cell(root: Path, symbol: str, fast: int, slow: int, pf: float,
                sharpe: float, trades: int):
    d = root / 'results' / symbol_dir_name(symbol) / f'P{fast}_{slow}'
    d.mkdir(parents=True, exist_ok=True)
    payload = {
        'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
        'net_profit_factor': pf, 'sharpe_ratio': sharpe, 'trade_count': trades,
        'gross_profit_factor': pf + 0.1, 'net_win_rate': 0.5,
    }
    (d / 'summary.json').write_text(json.dumps(payload))


def test_load_cells_and_aggregation(tmp_path):
    """Cells are discovered, aggregated per symbol and per pair."""
    root = tmp_path / 'run_grid'
    _write_cell(root, 'BTC/USDT', 8, 12, 1.2, 0.5, 100)
    _write_cell(root, 'BTC/USDT', 8, 20, 0.5, -0.2, 100)
    _write_cell(root, 'ETH/USDT', 8, 12, 0.9, 0.1, 100)
    _write_cell(root, 'ETH/USDT', 8, 20, 0.4, -0.3, 100)

    cells, blocked = load_cells(root)
    assert len(cells) == 4
    assert blocked == []

    sym_rows = per_symbol_table(cells, order=['BTC/USDT', 'ETH/USDT'])
    assert [r['symbol'] for r in sym_rows] == ['BTC/USDT', 'ETH/USDT']
    assert sym_rows[0]['n_cells_net_pf_gt_1'] == 1
    assert sym_rows[0]['frac_cells_net_pf_gt_1'] == 0.5
    assert sym_rows[0]['best_cell'] == 'P8_12'
    assert sym_rows[1]['best_net_pf'] == 0.9

    pair_rows = per_pair_table(cells)
    by_pair = {(r['P_fast'], r['P_slow']): r for r in pair_rows}
    assert by_pair[(8, 12)]['n_symbols'] == 2
    assert by_pair[(8, 12)]['n_symbols_net_pf_gt_1'] == 1
    assert by_pair[(8, 20)]['n_symbols_net_pf_gt_1'] == 0


def test_load_cells_reports_blocked(tmp_path):
    """A cell that errored is surfaced as blocked, not silently dropped."""
    root = tmp_path / 'run_grid'
    d = root / 'results' / 'BTC_USDT' / 'P8_12'
    d.mkdir(parents=True)
    (d / 'blocked.json').write_text(json.dumps(
        {'symbol': 'BTC/USDT', 'P_fast': 8, 'P_slow': 12, 'reason': 'boom'}))
    cells, blocked = load_cells(root)
    assert cells == []
    assert len(blocked) == 1
    assert blocked[0]['reason'] == 'boom'


@pytest.mark.parametrize('pf,sharpe,trades,expected', [
    (1.5, 1.0, 100, 'exploratory signal'),
    (1.05, 0.2, 40, 'exploratory signal'),
    (0.9, 0.5, 100, 'rejected'),
    (1.5, 0.5, 5, 'rejected'),
    (1.5, -0.1, 100, 'rejected'),
])
def test_label_cell(pf, sharpe, trades, expected):
    assert label_cell({'net_profit_factor': pf, 'sharpe_ratio': sharpe,
                        'trade_count': trades}) == expected
