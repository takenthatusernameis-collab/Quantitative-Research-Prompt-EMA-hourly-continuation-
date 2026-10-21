"""Tests for the cost-drag decomposition leg."""
import numpy as np
import pandas as pd
import pytest

from scripts.cost_drag_leg import (UNCAPPED_MULTIPLE, cap_risk_threshold,
                                    cost_per_side, decompose, model_cost_ratio,
                                    pooled_decompose, sample_cells,
                                    trades_frame)
from scripts.run_grid import CONFIG_DEFAULTS


def make_trades(rows):
    """A trade blotter with the columns the decomposition reads."""
    return pd.DataFrame(rows)


def test_cost_per_side_matches_the_engine():
    config = dict(CONFIG_DEFAULTS)
    assert cost_per_side(config) == pytest.approx(12.0 / 10000.0)


def test_cap_threshold_is_the_engine_condition():
    """The cap binds when the requested notional exceeds the cap."""
    config = dict(CONFIG_DEFAULTS)
    # qty = equity * risk_fraction / risk, notional = qty * price
    # cap binds <=> price / risk > max_notional_multiple / risk_fraction
    threshold = cap_risk_threshold(config)
    assert threshold == pytest.approx(config['risk_fraction']
                                      / config['max_notional_multiple'])
    # just above the threshold the requested notional fits under the cap
    risk_pct = threshold * 1.01
    assert (config['risk_fraction'] / risk_pct) <= config['max_notional_multiple']
    # just below it the cap binds
    risk_pct = threshold * 0.99
    assert (config['risk_fraction'] / risk_pct) > config['max_notional_multiple']


def test_cap_threshold_without_a_cap_is_infinite():
    config = dict(CONFIG_DEFAULTS)
    config['max_notional_multiple'] = UNCAPPED_MULTIPLE
    assert cap_risk_threshold(config) < 1e-6


def test_model_cost_ratio_is_inversely_proportional_to_the_risk():
    config = dict(CONFIG_DEFAULTS)
    wide = model_cost_ratio(0.01, config)
    narrow = model_cost_ratio(0.0025, config)
    assert wide == pytest.approx(0.24)
    assert narrow == pytest.approx(0.96)
    assert narrow == pytest.approx(4 * wide)


def test_decompose_splits_gross_cost_and_net():
    config = dict(CONFIG_DEFAULTS)
    trades = make_trades([
        {'bar_index': 0, 'pnl': 100.0, 'pnl_net': 90.0, 'entry_cost': 5.0,
         'exit_cost': 5.0, 'risk_pct': 0.01, 'notional': 1000.0, 'qty': 1.0},
        {'bar_index': 0, 'pnl': -50.0, 'pnl_net': -60.0, 'entry_cost': 5.0,
         'exit_cost': 5.0, 'risk_pct': 0.01, 'notional': 1000.0, 'qty': 1.0},
    ])
    stats = decompose(trades, config)
    assert stats['trades'] == 2
    assert stats['gross_pf'] == pytest.approx(2.0)
    assert stats['net_pf'] == pytest.approx(90.0 / 60.0)
    assert stats['cost_total'] == pytest.approx(20.0)
    assert stats['gross_pnl'] == pytest.approx(50.0)
    assert stats['net_pnl'] == pytest.approx(30.0)
    # the costs take 20 of the 150 of gross P&L that moved
    assert stats['cost_share_of_gross'] == pytest.approx(20.0 / 150.0)
    assert stats['capped_trade_share'] == pytest.approx(0.0)


def test_decompose_flags_the_capped_trades():
    config = dict(CONFIG_DEFAULTS)
    threshold = cap_risk_threshold(config)
    trades = make_trades([
        {'bar_index': 0, 'pnl': 10.0, 'pnl_net': 1.0, 'entry_cost': 4.5,
         'exit_cost': 4.5, 'risk_pct': threshold * 0.5, 'notional': 1000.0,
         'qty': 1.0},
        {'bar_index': 0, 'pnl': 10.0, 'pnl_net': 8.0, 'entry_cost': 1.0,
         'exit_cost': 1.0, 'risk_pct': 0.02, 'notional': 1000.0, 'qty': 1.0},
    ])
    stats = decompose(trades, config)
    assert stats['capped_trade_share'] == pytest.approx(0.5)


def test_decompose_of_an_empty_blotter_is_missing_evidence():
    config = dict(CONFIG_DEFAULTS)
    stats = decompose(pd.DataFrame(), config)
    assert stats['trades'] == 0
    assert stats['gross_pf'] is None
    assert stats['net_pf'] is None


def test_pooled_decompose_weights_cells_by_trades():
    """A mean of per-cell ratios would give a thin cell the same weight."""
    config = dict(CONFIG_DEFAULTS)
    thick = make_trades([
        {'bar_index': 0, 'pnl': 100.0, 'pnl_net': 100.0, 'entry_cost': 0.0,
         'exit_cost': 0.0, 'risk_pct': 0.01, 'notional': 1000.0, 'qty': 1.0},
    ])
    thin = make_trades([
        {'bar_index': 0, 'pnl': -100.0, 'pnl_net': -100.0, 'entry_cost': 0.0,
         'exit_cost': 0.0, 'risk_pct': 0.01, 'notional': 1000.0, 'qty': 1.0},
    ])
    pooled = pooled_decompose([thick, thin], config)
    assert pooled['cells'] == 2
    assert pooled['trades'] == 2
    assert pooled['gross_pf'] == pytest.approx(1.0)


def test_trades_frame_keeps_the_columns_the_decomposition_reads():
    class FakeTrade:
        side = 'long'
        entry_time = exit_time = 0
        entry_price = exit_price = 1.0
        sl = tp = risk = 1.0
        pnl = pnl_net = 0.0
        exit_reason = 'tp'
        bar_index = 0
        exit_bar_index = 1
        qty = notional = 1.0
        entry_cost = exit_cost = 0.0
        risk_pct = 0.01

    frame = trades_frame([FakeTrade()])
    for column in ('pnl', 'pnl_net', 'entry_cost', 'exit_cost', 'risk_pct'):
        assert column in frame.columns


def test_sample_cells_takes_one_cell_per_symbol(tmp_path):
    import json
    run = tmp_path / 'results'
    for index, symbol in enumerate(('AAA_USDT', 'BBB_USDT', 'CCC_USDT')):
        for fast, slow in ((8, 12), (20, 50)):
            cell = run / symbol / f'P{fast}_{slow}'
            cell.mkdir(parents=True)
            (cell / 'summary.json').write_text(json.dumps({'net_profit_factor': 1.0}))
    sample = sample_cells(tmp_path, 2, 'data/fixtures')
    assert len(sample) == 2
    assert [s[0] for s in sample] == ['AAA/USDT', 'BBB/USDT']
    # the sample is taken in market-cap (directory) order
    assert sample[0][1] < sample[0][2]
