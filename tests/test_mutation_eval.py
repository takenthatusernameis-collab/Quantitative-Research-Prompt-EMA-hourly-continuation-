"""Tests for the parent -> child -> delta evaluation of a grid mutation."""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from scripts.mutation_eval import (MUTATION_KEYS, cell_statistics, complete_symbols,
                                    config_delta, pooled_pf, restrict_to_common_cells,
                                    verify_sample)
from scripts.run_grid import CONFIG_DEFAULTS, period_pairs, run_cell, symbol_dir_name

PAIRS = period_pairs()


def write_fixture(path: Path, n_bars: int = 900) -> None:
    rng = np.random.default_rng(11)
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


def test_config_delta_reports_a_single_variable_mutation():
    parent = dict(CONFIG_DEFAULTS)
    child = dict(CONFIG_DEFAULTS)
    child['min_risk_atr'] = True
    delta = config_delta(parent, child)
    assert delta['changed_keys'] == ['min_risk_atr']
    assert delta['single_variable'] is True
    assert delta['changed']['min_risk_atr'] == {'parent': False, 'child': True}


def test_config_delta_rejects_a_multi_variable_change():
    parent = dict(CONFIG_DEFAULTS)
    child = dict(CONFIG_DEFAULTS)
    child['min_risk_atr'] = True
    child['taker_fee_bps'] = 20.0
    delta = config_delta(parent, child)
    assert set(delta['changed_keys']) == {'min_risk_atr', 'taker_fee_bps'}
    assert delta['single_variable'] is False


def test_config_delta_of_an_unchanged_config_is_not_a_mutation():
    delta = config_delta(dict(CONFIG_DEFAULTS), dict(CONFIG_DEFAULTS))
    assert delta['changed_keys'] == []
    assert delta['single_variable'] is False


def test_pooled_pf_uses_the_sums_not_the_ratios():
    assert pooled_pf(10.0, 5.0) == 2.0
    # only losses: the ratio is defined and it is zero
    assert pooled_pf(0.0, 5.0) == 0.0
    # no trades at all: the ratio is undefined, not zero
    assert pooled_pf(0.0, 0.0) is None
    assert pooled_pf(5.0, 0.0) == float('inf')


def test_complete_symbols_only_counts_finished_grids(tmp_path):
    run_dir = tmp_path / 'run'
    (run_dir / 'results' / 'A_USDT' / f'P{PAIRS[0][0]}_{PAIRS[0][1]}').mkdir(parents=True)
    assert complete_symbols(run_dir, ['A/USDT', 'B/USDT']) == []


def test_restrict_to_common_cells_keeps_the_intersection():
    parent = {'rows': [{'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 12},
                        {'symbol': 'A/USDT', 'P_fast': 12, 'P_slow': 21}],
              'fold_rows': [{'symbol': 'A/USDT', 'P_fast': 8, 'P_slow': 12},
                            {'symbol': 'A/USDT', 'P_fast': 12, 'P_slow': 21}]}
    child = {'rows': [{'symbol': 'A/USDT', 'P_fast': 12, 'P_slow': 21},
                       {'symbol': 'A/USDT', 'P_fast': 20, 'P_slow': 26}],
             'fold_rows': [{'symbol': 'A/USDT', 'P_fast': 12, 'P_slow': 21},
                           {'symbol': 'A/USDT', 'P_fast': 20, 'P_slow': 26}]}
    restrict_to_common_cells(parent, child)
    assert len(parent['rows']) == 1
    assert len(child['rows']) == 1
    assert parent['rows'][0]['P_fast'] == 12


def test_cell_statistics_and_verification_reproduce_the_stored_summary(tmp_path):
    """The evaluation reads the blotters; they have to agree with the summary."""
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    child_cfg = dict(CONFIG_DEFAULTS)
    child_cfg['min_risk_atr'] = True
    run_dir = tmp_path / 'run'
    build_run(run_dir, fixture_base, 'TEST/USDT', child_cfg)

    stats = cell_statistics(run_dir, ['TEST/USDT'], str(fixture_base), 0.35, 2.0, 5, 30)
    assert len(stats['rows']) == len(PAIRS)
    assert len(stats['fold_rows']) == len(PAIRS)
    for row in stats['rows']:
        assert row['stored_net_pf'] == pytest.approx(row['net_pf'], rel=1e-9, abs=1e-9)

    verified = verify_sample(run_dir, child_cfg, ['TEST/USDT'], str(fixture_base), 1)
    assert len(verified) == 1
    assert verified[0]['max_abs_delta'] == 0.0


def test_the_mutation_removes_trades(tmp_path):
    """The ATR filter can only remove entries, never add them."""
    fixture_base = tmp_path / 'fixtures'
    write_fixture(fixture_base / 'TEST_USDT.csv')
    parent_cfg = dict(CONFIG_DEFAULTS)
    child_cfg = dict(CONFIG_DEFAULTS)
    child_cfg['min_risk_atr'] = True
    parent_dir = tmp_path / 'parent'
    child_dir = tmp_path / 'child'
    build_run(parent_dir, fixture_base, 'TEST/USDT', parent_cfg)
    build_run(child_dir, fixture_base, 'TEST/USDT', child_cfg)
    parent_stats = cell_statistics(parent_dir, ['TEST/USDT'], str(fixture_base),
                                   0.35, 2.0, 5, 30)
    child_stats = cell_statistics(child_dir, ['TEST/USDT'], str(fixture_base),
                                  0.35, 2.0, 5, 30)
    parent_trades = sum(r['trades'] for r in parent_stats['rows'])
    child_trades = sum(r['trades'] for r in child_stats['rows'])
    assert child_trades <= parent_trades
