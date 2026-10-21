"""Tests for the full EMA grid runner and grid aggregation."""
import gzip
import itertools
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts.run_grid import (
    EQUITY_FILENAME,
    GRID_PAIRS,
    PERIOD_GRID,
    TRADES_FILENAME,
    merge_symbol_lists,
    period_pairs,
    read_artifact_csv,
    symbol_dir_name,
    write_csv_gz,
)
from scripts.aggregate_grid import label_cell, load_cells, per_pair_table, per_symbol_table


def test_merge_symbol_lists_keeps_prior_coverage():
    """A narrower resume must not shrink the recorded coverage of a run.

    A resume with a smaller `--n` used to overwrite progress.json with the
    narrower symbol list while the completed-cell set stayed at the full grid,
    so the state file contradicted itself and the handoff lost symbols.
    """
    assert merge_symbol_lists(['A/USDT', 'B/USDT'], ['A/USDT']) == ['A/USDT', 'B/USDT']
    assert merge_symbol_lists(['A/USDT'], ['A/USDT', 'C/USDT']) == ['A/USDT', 'C/USDT']
    assert merge_symbol_lists([], ['A/USDT']) == ['A/USDT']
    assert merge_symbol_lists(None, None) == []


def test_canonical_grid_progress_is_internally_consistent():
    """The durable progress record of the shipped grid run stays consistent.

    Every recorded symbol must be covered by the completed cells, and the cell
    count must match symbols x pairs.
    """
    progress_path = Path('results/20261019_135940_grid/progress.json')
    if not progress_path.exists():
        pytest.skip('canonical grid run not present')
    progress = json.loads(progress_path.read_text())
    symbols = progress['symbols']
    assert progress['n_symbols'] == len(symbols)
    assert progress['completed_cells'] == len(progress['completed'])
    assert progress['n_symbols'] * progress['n_pairs'] == progress['completed_cells']
    assert {c['symbol'] for c in progress['completed']} <= set(symbols)


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


def test_bulk_artifacts_are_gzip_compressed_and_lossless(tmp_path):
    """Bulk per-cell artifacts are gzip CSVs so checkpoints stay inside the
    controller's 30s remote-push budget. Content must round-trip exactly."""
    df = pd.DataFrame({
        'index': [0, 1, 2],
        'timestamp': ['2024-01-01 00:00:00+00:00'] * 3,
        'equity': [10000.0, 10001.5, 9999.25],
        'position': [0, 1, -1],
    })
    path = tmp_path / TRADES_FILENAME
    write_csv_gz(df, path)

    assert path.exists()
    with open(path, 'rb') as fh:
        assert fh.read(2) == b'\x1f\x8b'  # gzip magic
    restored = read_artifact_csv(path)
    pd.testing.assert_frame_equal(restored, df)


def test_gzip_artifacts_are_byte_deterministic(tmp_path):
    """Identical cells must produce identical blobs so git can delta them."""
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['x', 'y', 'z']})
    first = tmp_path / 'a.csv.gz'
    second = tmp_path / 'b.csv.gz'
    write_csv_gz(df, first)
    write_csv_gz(df, second)
    assert first.read_bytes() == second.read_bytes()


def test_read_artifact_csv_handles_plain_csv(tmp_path):
    """Artifacts written before compression used plain CSV and stay readable."""
    path = tmp_path / 'trades.csv'
    pd.DataFrame({'a': [1, 2]}).to_csv(path, index=False)
    restored = read_artifact_csv(path)
    assert list(restored['a']) == [1, 2]


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


def test_fast_engine_reproduces_the_reference_engine():
    """The `fast` engine has to be a drop-in twin of the reference engine.

    The ATR minimum-risk mutation is run on the fast engine (the reference
    engine needs ~44 h for the full grid), so the two have to agree on the
    cells that the mutation actually changes: the trades the ATR filter
    keeps, and the metrics that follow from them.
    """
    from pathlib import Path

    from data.data_loader import load_ohlcv_csv
    from scripts.run_grid import CONFIG_DEFAULTS, run_cell

    fixture = Path('data/fixtures/1INCH_USDT.csv')
    if not fixture.exists():
        pytest.skip('fixture not available')
    df = load_ohlcv_csv(str(fixture))
    config = CONFIG_DEFAULTS
    for min_risk_atr in (False, True):
        args = ('1INCH/USDT', df, 8, 200, config['taker_fee_bps'],
                config['slippage_bps'], config['rr'], config['stricter_trend'],
                min_risk_atr, config['atr_threshold'], config['conservative_exit'])
        _, _, reference = run_cell(*args, engine='reference')
        _, _, fast = run_cell(*args, engine='fast')
        assert reference['trade_count'] == fast['trade_count']
        assert reference['net_profit_factor'] == fast['net_profit_factor']
        assert reference['sharpe_ratio'] == fast['sharpe_ratio']
        assert reference['max_drawdown'] == fast['max_drawdown']
