"""Tests for the survivor check of a mutation child grid."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from scripts.mutation_survivor_check import (build_verdict, cell_rows,
                                              family_pooled,
                                              leave_one_symbol_out,
                                              percentile_rank, subperiod_stability)
from scripts.run_grid import CONFIG_DEFAULTS, period_pairs, run_cell, symbol_dir_name

PAIRS = period_pairs()


def write_fixture(path: Path, n_bars: int = 1200) -> None:
    rng = np.random.default_rng(31)
    close = 100.0 + np.cumsum(rng.normal(0.0, 0.6, n_bars))
    df = pd.DataFrame({
        'timestamp': pd.date_range('2023-01-01', periods=n_bars, freq='h'),
        'open': close,
        'high': close + 0.4,
        'low': close - 0.4,
        'close': close,
        'volume': 100.0 + rng.random(n_bars),
    })
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_run(run_dir: Path, fixture_base: Path, symbol: str, config: dict) -> None:
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


def test_cell_rows_reads_the_grid_and_scores_the_out_of_sample_window(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    cfg = dict(CONFIG_DEFAULTS)
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', cfg)

    rows = cell_rows(run_dir, ['TEST/USDT'], str(fixture_base), 0.35, 2.0, 30)
    assert len(rows) == len(PAIRS)
    for row in rows:
        assert row['n_bars'] == 1200
        assert row['entry_start_index'] == int(1200 * 0.65)
        assert row['oos_trades'] <= row['n_bars']
        assert isinstance(row['clears_gate'], bool)


def test_family_pooled_uses_the_sums_not_the_ratios():
    rows = [{'oos_win_sum': 10.0, 'oos_loss_abs': 5.0, 'oos_trades': 3},
            {'oos_win_sum': 30.0, 'oos_loss_abs': 10.0, 'oos_trades': 7}]
    pooled = family_pooled(rows)
    assert pooled['pooled_oos_net_pf'] == 40.0 / 15.0
    assert pooled['trades'] == 10


def test_leave_one_symbol_out_reports_the_family_without_each_symbol():
    rows = [
        {'symbol': 'A/USDT', 'oos_win_sum': 10.0, 'oos_loss_abs': 5.0,
         'oos_trades': 2, 'clears_gate': True},
        {'symbol': 'B/USDT', 'oos_win_sum': 1.0, 'oos_loss_abs': 9.0,
         'oos_trades': 2, 'clears_gate': False},
    ]
    out = leave_one_symbol_out(rows)
    by_symbol = {row['dropped_symbol']: row for row in out}
    assert by_symbol['A/USDT']['cells_left'] == 1
    assert by_symbol['A/USDT']['gate_cells_left'] == 0
    assert by_symbol['B/USDT']['cells_left'] == 1
    assert by_symbol['B/USDT']['gate_cells_left'] == 1


def test_percentile_rank_counts_the_values_below():
    assert percentile_rank(2.0, [1.0, 2.0, 3.0]) == 1 / 3
    assert percentile_rank(0.0, [1.0, 2.0]) == 0.0
    assert percentile_rank(1.0, []) is None


def test_subperiod_stability_splits_the_out_of_sample_window(tmp_path):
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    cfg = dict(CONFIG_DEFAULTS)
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', cfg)

    rows = cell_rows(run_dir, ['TEST/USDT'], str(fixture_base), 0.35, 2.0, 30)
    row = rows[0]
    row['clears_gate'] = True
    out = subperiod_stability(run_dir, [row], 4, 2.0)
    assert len(out) == 1
    assert out[0]['n_subperiods'] == 4
    assert out[0]['subperiods_with_trades'] <= 4
    assert isinstance(out[0]['stable'], bool)


def test_the_verdict_does_not_call_a_gate_family_stable_when_it_is_not():
    payload = {
        'n_cells': 100, 'n_gate_cells': 4, 'n_gate_symbols': 2,
        'gate_by_symbol': {'A/USDT': 3, 'B/USDT': 1},
        'family': {'pooled_oos_net_pf': 1.2, 'trades': 300},
        'share_of_cells_oos_pf_gt_1': 0.3, 'n_stable_cells': 0,
        'subperiod_stability': [],
    }
    verdict = ' '.join(build_verdict(payload))
    assert 'the family is a time artefact' in verdict
    assert 'not a promotion' in verdict


def test_the_verdict_names_the_stable_cells_when_there_are_some():
    payload = {
        'n_cells': 100, 'n_gate_cells': 4, 'n_gate_symbols': 2,
        'gate_by_symbol': {'A/USDT': 3, 'B/USDT': 1},
        'family': {'pooled_oos_net_pf': 1.2, 'trades': 300},
        'share_of_cells_oos_pf_gt_1': 0.3, 'n_stable_cells': 1,
        'subperiod_stability': [
            {'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 200, 'stable': True},
            {'symbol': 'B/USDT', 'P_fast': 8, 'P_slow': 200, 'stable': False},
        ],
    }
    verdict = ' '.join(build_verdict(payload))
    assert 'A/USDT P8_200' in verdict
    assert 'the other 3 work in one stretch of time only' in verdict
