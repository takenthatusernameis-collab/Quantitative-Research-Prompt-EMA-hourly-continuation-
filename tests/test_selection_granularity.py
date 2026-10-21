"""Tests for the selection-granularity leg."""
import json

import pytest

from scripts.selection_granularity import (market_cap_buckets, rank_symbols,
                                            score_unit, select, summarize,
                                            unit_candidates, unit_of,
                                            walk_forward)


def fold(fold_id, trades, win, loss, s_win=None, s_loss=None):
    """One fold of a cell's statistics."""
    return {'fold': fold_id, 'trades': trades, 'win_sum': win, 'loss_abs': loss,
            'stress_win_sum': win if s_win is None else s_win,
            'stress_loss_abs': loss if s_loss is None else s_loss}


def cell(symbol, fast, slow, folds):
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'n_bars': 1000, 'folds': folds}


def test_market_cap_buckets_are_contiguous_and_ordered():
    symbols = [f'S{i}/USDT' for i in range(10)]
    buckets = market_cap_buckets(symbols, 5)
    assert [buckets[f'S{i}/USDT'] for i in range(10)] == [
        'B00', 'B00', 'B01', 'B01', 'B02', 'B02', 'B03', 'B03', 'B04', 'B04']
    # The buckets hold every symbol exactly once.
    assert set(buckets.values()) == {'B00', 'B01', 'B02', 'B03', 'B04'}


def test_unit_of():
    buckets = {'A/USDT': 'B00', 'B/USDT': 'B01'}
    assert unit_of('A/USDT', 'symbol', buckets) == 'A/USDT'
    assert unit_of('A/USDT', 'bucket', buckets) == 'B00'
    assert unit_of('A/USDT', 'global', buckets) == 'GLOBAL'
    with pytest.raises(ValueError):
        unit_of('A/USDT', 'nonsense', buckets)


def test_rank_symbols_uses_the_universe_ranking(tmp_path):
    path = tmp_path / 'mcap.json'
    path.write_text(json.dumps({'symbols': ['B/USDT', 'A/USDT', 'C/USDT']}))
    assert rank_symbols(str(path), ['A/USDT', 'C/USDT', 'B/USDT']) == [
        'B/USDT', 'A/USDT', 'C/USDT']
    # A symbol the ranking does not know keeps a deterministic place.
    assert rank_symbols(str(path), ['A/USDT', 'Z/USDT']) == ['A/USDT', 'Z/USDT']


def test_unit_candidates_pool_the_history_over_the_unit():
    """The history of a candidate pair is pooled over the unit's symbols."""
    cells = {
        'A/USDT': [cell('A/USDT', 8, 20, [fold(0, 10, 6.0, 4.0), fold(1, 5, 3.0, 2.0)]),
                   cell('A/USDT', 8, 50, [fold(0, 10, 4.0, 6.0), fold(1, 5, 2.0, 3.0)])],
        'B/USDT': [cell('B/USDT', 8, 20, [fold(0, 10, 9.0, 1.0), fold(1, 5, 4.0, 1.0)]),
                   cell('B/USDT', 8, 50, [fold(0, 10, 4.0, 6.0), fold(1, 5, 2.0, 3.0)])],
    }
    candidates = unit_candidates(cells, 1, min_history_trades=1)
    by_pair = {(c['P_fast'], c['P_slow']): c for c in candidates}
    # Step 1 uses fold 0 as history: P8_20 wins (15.0/5.0), P8_50 does not (8/12).
    assert by_pair[(8, 20)]['net_pf'] == pytest.approx(15.0 / 5.0)
    assert by_pair[(8, 50)]['net_pf'] == pytest.approx(8.0 / 12.0)
    assert select(candidates, 1)[0]['P_slow'] == 20

    # Step 2 uses folds 0 and 1 as history.
    candidates = unit_candidates(cells, 2, min_history_trades=1)
    by_pair = {(c['P_fast'], c['P_slow']): c for c in candidates}
    assert by_pair[(8, 20)]['net_pf'] == pytest.approx(22.0 / 8.0)
    assert by_pair[(8, 50)]['net_pf'] == pytest.approx(12.0 / 18.0)


def test_unit_candidates_needs_enough_history_trades_per_symbol():
    cells = {'A/USDT': [cell('A/USDT', 8, 20, [fold(0, 5, 3.0, 2.0), fold(1, 1, 1.0, 0.0)])]}
    assert unit_candidates(cells, 1, min_history_trades=20) == []
    assert unit_candidates(cells, 1, min_history_trades=1) != []


def test_score_unit_scores_the_test_fold_only():
    cells = {
        'A/USDT': [cell('A/USDT', 8, 20, [fold(0, 10, 6.0, 4.0), fold(1, 7, 5.0, 2.0)]),
                   cell('A/USDT', 8, 50, [fold(0, 10, 9.0, 1.0), fold(1, 7, 1.0, 6.0)])],
    }
    selected = [{'P_fast': 8, 'P_slow': 20, 'trades': 10, 'net_pf': 1.5}]
    score = score_unit(cells, selected, 1)
    assert score['trades'] == 7
    assert score['net_pf'] == pytest.approx(5.0 / 2.0)
    # A pair that was not selected contributes nothing.
    selected = [{'P_fast': 8, 'P_slow': 50, 'trades': 10, 'net_pf': 9.0}]
    score = score_unit(cells, selected, 1)
    assert score['net_pf'] == pytest.approx(1.0 / 6.0)


def test_walk_forward_never_scores_the_history_fold():
    """Step k scores fold k, which the selection at step k never saw."""
    folds = [fold(0, 10, 9.0, 1.0), fold(1, 10, 1.0, 9.0)]
    rows = [cell('A/USDT', 8, 20, folds)]
    steps = walk_forward(rows, 'symbol', 1, 2, 1, {})
    assert len(steps) == 1
    assert steps[0]['step'] == 1
    # The history is fold 0 (PF 9.0), the score is fold 1 (PF 1/9).
    assert steps[0]['history_net_pf'] == pytest.approx(9.0)
    assert steps[0]['oof_net_pf'] == pytest.approx(1.0 / 9.0)


def test_walk_forward_global_unit_selects_once_for_every_symbol():
    folds_good = [fold(0, 10, 9.0, 1.0), fold(1, 10, 9.0, 1.0)]
    folds_bad = [fold(0, 10, 1.0, 9.0), fold(1, 10, 1.0, 9.0)]
    rows = [cell('A/USDT', 8, 20, folds_good), cell('A/USDT', 8, 50, folds_bad),
            cell('B/USDT', 8, 20, folds_good), cell('B/USDT', 8, 50, folds_bad)]
    steps = walk_forward(rows, 'global', 1, 2, 1, {})
    assert len(steps) == 1
    assert steps[0]['unit_name'] == 'GLOBAL'
    assert steps[0]['symbols'] == 2
    assert steps[0]['selected'][0]['P_slow'] == 20
    # Both symbols are scored with the selected pair.
    assert steps[0]['oof_trades'] == 20
    assert steps[0]['oof_net_pf'] == pytest.approx(18.0 / 2.0)


def test_summarize_pools_the_out_of_fold_trades():
    steps = [
        {'step': 1, 'unit_name': 'A/USDT', 'scored': True, 'oof_trades': 10,
         'oof_net_pf': 1.2, 'oof_stress_net_pf': 1.1, 'oof_win_sum': 12.0,
         'oof_loss_abs': 10.0, 'oof_stress_win_sum': 11.0, 'oof_stress_loss_abs': 10.0,
         'history_net_pf': 1.4},
        {'step': 1, 'unit_name': 'B/USDT', 'scored': True, 'oof_trades': 20,
         'oof_net_pf': 0.8, 'oof_stress_net_pf': 0.7, 'oof_win_sum': 8.0,
         'oof_loss_abs': 10.0, 'oof_stress_win_sum': 7.0, 'oof_stress_loss_abs': 10.0,
         'history_net_pf': 1.1},
    ]
    summary = summarize(steps)
    assert summary['oof_trades'] == 30
    assert summary['pooled_oof_net_pf'] == pytest.approx(20.0 / 20.0)
    assert summary['pooled_oof_stress_net_pf'] == pytest.approx(18.0 / 20.0)
    assert summary['oof_pf_gt_1'] == 1
    assert summary['oof_pf_gt_1_share'] == pytest.approx(0.5)
    assert summary['median_history_pf'] == pytest.approx(1.25)
