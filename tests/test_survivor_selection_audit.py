"""Tests for the survivor selection audit leg."""
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from scripts.survivor_selection_audit import (CLOSEST_SURVIVORS, binomial_upper_tail,
                                              cell_fold_stats, family_pooled,
                                              fold_edges, fold_of,
                                              leave_one_symbol_out, null_pf_distribution,
                                              oos_subperiods, percentile_rank,
                                              pooled_pf, select_best,
                                              survivor_cells, sum_folds,
                                              walk_forward_steps)


def make_trades(rows):
    """A trade blotter with the columns the leg reads."""
    return pd.DataFrame(rows)


def trade(bar, pnl_net, entry_cost=0.0, exit_cost=0.0):
    return {'bar_index': bar, 'pnl': pnl_net, 'pnl_net': pnl_net,
            'entry_cost': entry_cost, 'exit_cost': exit_cost}


def screen_row(symbol, fast, slow, oos_pf, oos_trades, stress_pf=None,
               win=None, loss=None):
    return {
        'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
        'oos_net_pf': oos_pf, 'oos_trades': oos_trades,
        'oos_stress_net_pf': stress_pf if stress_pf is not None else oos_pf,
        'oos_win_sum': win if win is not None else oos_pf,
        'oos_loss_abs': loss if loss is not None else 1.0,
        'oos_stress_win_sum': win if win is not None else oos_pf,
        'oos_stress_loss_abs': loss if loss is not None else 1.0,
        'net_pf': 0.9, 'stress_net_pf': 0.7,
        'n_bars': 1000, 'entry_start_index': 650,
    }


def test_fold_edges_partition_the_sample():
    edges = fold_edges(22000, 5)
    assert edges == [0, 4400, 8800, 13200, 17600, 22000]
    assert edges[0] == 0 and edges[-1] == 22000
    assert edges == sorted(edges)


def test_fold_of_places_a_bar_in_the_right_fold():
    edges = fold_edges(100, 4)
    assert fold_of(0, edges) == 0
    assert fold_of(24, edges) == 0
    assert fold_of(25, edges) == 1
    assert fold_of(99, edges) == 3
    # a bar beyond the last edge still lands in the last fold
    assert fold_of(150, edges) == 3


def test_cell_fold_stats_assigns_a_trade_to_its_entry_fold():
    trades = make_trades([trade(0, 10.0), trade(50, -4.0), trade(99, 6.0)])
    edges = fold_edges(100, 4)
    stats = cell_fold_stats(trades, edges)
    # edges are [0, 25, 50, 75, 100): the bars 0, 50 and 99 land in folds 0, 2 and 3
    assert [s['trades'] for s in stats] == [1, 0, 1, 1]
    assert stats[0]['win_sum'] == pytest.approx(10.0)
    assert stats[2]['loss_abs'] == pytest.approx(4.0)
    assert stats[3]['win_sum'] == pytest.approx(6.0)


def test_cell_fold_stats_charges_the_stress_cost():
    trades = make_trades([trade(0, 10.0, entry_cost=1.0, exit_cost=1.0)])
    stats = cell_fold_stats(trades, fold_edges(100, 4), stress_multiplier=2.0)
    # 2x costs subtract one more (entry + exit) cost from the trade
    assert stats[0]['win_sum'] == pytest.approx(10.0)
    assert stats[0]['stress_win_sum'] == pytest.approx(8.0)


def test_cell_fold_stats_of_an_empty_blotter_is_missing_evidence():
    stats = cell_fold_stats(pd.DataFrame(), fold_edges(100, 4))
    assert [s['trades'] for s in stats] == [0, 0, 0, 0]


def test_sum_folds_aggregates_the_history_window():
    folds = [{'trades': 2, 'win_sum': 10.0, 'loss_abs': 1.0,
              'stress_win_sum': 8.0, 'stress_loss_abs': 2.0},
             {'trades': 3, 'win_sum': 5.0, 'loss_abs': 2.0,
              'stress_win_sum': 3.0, 'stress_loss_abs': 4.0},
             {'trades': 1, 'win_sum': 1.0, 'loss_abs': 1.0,
              'stress_win_sum': 1.0, 'stress_loss_abs': 1.0}]
    hist = sum_folds(folds, 2)
    assert hist['trades'] == 5
    assert hist['net_pf'] == pytest.approx(15.0 / 3.0)
    assert hist['stress_net_pf'] == pytest.approx(11.0 / 6.0)


def test_select_best_breaks_ties_on_the_thicker_sample():
    candidates = [
        {'P_fast': 8, 'P_slow': 200, 'net_pf': 1.2, 'trades': 10},
        {'P_fast': 20, 'P_slow': 200, 'net_pf': 1.2, 'trades': 40},
        {'P_fast': 50, 'P_slow': 200, 'net_pf': 0.9, 'trades': 100},
    ]
    assert select_best(candidates)['P_fast'] == 20


def test_select_best_ignores_a_cell_without_profit_factor():
    candidates = [{'P_fast': 8, 'P_slow': 200, 'net_pf': None, 'trades': 10}]
    assert select_best(candidates) is None


def test_walk_forward_scores_the_selection_on_an_unseen_fold():
    # Cell A is the best on the history, cell B is better on the test fold.
    cells = [
        {'P_fast': 8, 'P_slow': 200, 'folds': [
            {'trades': 30, 'win_sum': 60.0, 'loss_abs': 10.0,
             'stress_win_sum': 55.0, 'stress_loss_abs': 15.0},
            {'trades': 10, 'win_sum': 1.0, 'loss_abs': 9.0,
             'stress_win_sum': 1.0, 'stress_loss_abs': 9.0},
        ]},
        {'P_fast': 20, 'P_slow': 200, 'folds': [
            {'trades': 30, 'win_sum': 40.0, 'loss_abs': 20.0,
             'stress_win_sum': 35.0, 'stress_loss_abs': 25.0},
            {'trades': 10, 'win_sum': 20.0, 'loss_abs': 1.0,
             'stress_win_sum': 18.0, 'stress_loss_abs': 3.0},
        ]},
    ]
    steps = walk_forward_steps(cells, 2, min_history_trades=20)
    assert len(steps) == 1
    step = steps[0]
    # the history picks the cell with the better in-fold profit factor
    assert step['selected'] == (8, 200)
    # and it is scored on the fold the selection never saw
    assert step['oof_trades'] == 10
    assert step['oof_net_pf'] == pytest.approx(1.0 / 9.0)
    assert step['oof_stress_net_pf'] == pytest.approx(1.0 / 9.0)


def test_walk_forward_skips_a_cell_without_enough_history():
    cells = [
        {'P_fast': 8, 'P_slow': 200, 'folds': [
            {'trades': 3, 'win_sum': 60.0, 'loss_abs': 1.0,
             'stress_win_sum': 60.0, 'stress_loss_abs': 1.0},
            {'trades': 10, 'win_sum': 1.0, 'loss_abs': 9.0,
             'stress_win_sum': 1.0, 'stress_loss_abs': 9.0},
        ]},
    ]
    steps = walk_forward_steps(cells, 2, min_history_trades=20)
    assert steps[0]['selected'] is None


def test_survivor_cells_applies_the_gate():
    rows = [
        screen_row('AAA/USDT', 8, 200, 1.2, 40),          # passes
        screen_row('BBB/USDT', 8, 200, 1.2, 10),          # too few trades
        screen_row('CCC/USDT', 8, 200, 0.9, 40),          # profit factor too low
        screen_row('DDD/USDT', 8, 200, 1.2, 40, stress_pf=0.8),  # stress too low
    ]
    survivors = survivor_cells(rows, min_trades=30)
    assert [r['symbol'] for r in survivors] == ['AAA/USDT']


def test_family_pooled_weights_cells_by_their_trades():
    rows = [screen_row('AAA/USDT', 8, 200, 2.0, 100, win=100.0, loss=50.0),
            screen_row('BBB/USDT', 8, 200, 0.5, 10, win=5.0, loss=10.0)]
    pooled = family_pooled(rows)
    assert pooled['cells'] == 2
    assert pooled['trades'] == 110
    assert pooled['net_pf'] == pytest.approx(105.0 / 60.0)
    assert pooled['net_pnl'] == pytest.approx(45.0)


def test_leave_one_symbol_out_keeps_the_other_symbols():
    rows = [
        screen_row('AAA/USDT', 8, 200, 1.5, 40),
        screen_row('AAA/USDT', 20, 200, 1.4, 40),
        screen_row('BBB/USDT', 8, 200, 1.3, 40),
        screen_row('CCC/USDT', 8, 200, 1.1, 40),
        screen_row('DDD/USDT', 8, 200, 1.0, 40),
        screen_row('EEE/USDT', 8, 200, 0.9, 40),
    ]
    family = survivor_cells(rows, min_trades=30)
    # EEE does not clear the gate, so it is not part of the family
    assert len(family) == 4
    loso = leave_one_symbol_out(rows, family, top_k=3, min_trades=30)
    by_symbol = {r['dropped_symbol']: r for r in loso}
    assert by_symbol['AAA/USDT']['dropped_cells'] == 2
    assert by_symbol['AAA/USDT']['family_remaining'] == 2
    # the ranked family is re-selected without AAA, so DDD moves in
    assert by_symbol['AAA/USDT']['ranked_retained'] == 2
    entrants = [e['symbol'] for e in by_symbol['AAA/USDT']['ranked_entrants']]
    assert entrants == ['DDD/USDT']
    assert by_symbol['AAA/USDT']['ranked_family_clears_gates'] is True


def test_leave_one_symbol_out_reports_a_family_that_breaks():
    rows = [
        screen_row('AAA/USDT', 8, 200, 1.5, 40, win=150.0, loss=100.0),
        screen_row('BBB/USDT', 8, 200, 1.05, 40, win=10.0, loss=9.0),
    ]
    family = survivor_cells(rows, min_trades=30)
    loso = leave_one_symbol_out(rows, family, top_k=2, min_trades=30)
    by_symbol = {r['dropped_symbol']: r for r in loso}
    # without AAA the family is one cell that barely holds up
    assert by_symbol['AAA/USDT']['family_remaining'] == 1
    assert by_symbol['AAA/USDT']['family_remaining_net_pf'] == pytest.approx(10.0 / 9.0)


def test_percentile_rank_of_the_null_distribution():
    distribution = [0.1, 0.2, 0.3, 0.4, 0.5]
    assert percentile_rank(0.6, distribution) == pytest.approx(1.0)
    assert percentile_rank(0.0, distribution) == pytest.approx(0.0)
    assert percentile_rank(0.3, distribution) == pytest.approx(0.5)


def test_null_pf_distribution_is_the_grid_own_draw():
    rows = [
        {'symbol': 'AAA/USDT', 'folds': [
            {'trades': 1, 'win_sum': 2.0, 'loss_abs': 1.0,
             'stress_win_sum': 2.0, 'stress_loss_abs': 1.0},
            {'trades': 1, 'win_sum': 3.0, 'loss_abs': 1.0,
             'stress_win_sum': 3.0, 'stress_loss_abs': 1.0},
        ]},
        {'symbol': 'BBB/USDT', 'folds': [
            {'trades': 1, 'win_sum': 1.0, 'loss_abs': 1.0,
             'stress_win_sum': 1.0, 'stress_loss_abs': 1.0},
            {'trades': 1, 'win_sum': 0.5, 'loss_abs': 1.0,
             'stress_win_sum': 0.5, 'stress_loss_abs': 1.0},
        ]},
    ]
    assert null_pf_distribution(rows, 1) == [3.0, 0.5]
    assert null_pf_distribution(rows, 0) == [2.0, 1.0]


def test_binomial_upper_tail_is_the_upper_tail():
    # P(X >= 0) = 1 and P(X > trials) = 0
    assert binomial_upper_tail(0, 20, 0.05) == pytest.approx(1.0)
    assert binomial_upper_tail(21, 20, 0.05) == pytest.approx(0.0)
    # P(X >= 1) under p = 0.5 is 1 - 0.5^n
    assert binomial_upper_tail(1, 10, 0.5) == pytest.approx(1.0 - 0.5 ** 10)
    # P(X >= 10) under p = 0.5 is 1 / 1024
    assert binomial_upper_tail(10, 10, 0.5) == pytest.approx(1.0 / 1024)


def test_closest_survivors_are_the_registered_six():
    assert len(CLOSEST_SURVIVORS) == 6
    assert ('DEXE/USDT', 50, 200) in CLOSEST_SURVIVORS
    assert ('ZEN/USDT', 12, 200) in CLOSEST_SURVIVORS


def test_pooled_pf_of_an_empty_sample_is_undefined():
    assert pooled_pf(0.0, 0.0) is None
    assert pooled_pf(5.0, 0.0) == float('inf')
    assert pooled_pf(5.0, 2.0) == pytest.approx(2.5)


def test_oos_subperiods_splits_the_out_of_sample_window(tmp_path):
    from scripts.run_grid import write_csv_gz
    run_dir = tmp_path
    cell = run_dir / 'results' / 'AAA_USDT' / 'P8_200'
    cell.mkdir(parents=True)
    trades = make_trades([trade(0, 1.0), trade(700, 2.0), trade(800, -1.0),
                          trade(900, -2.0), trade(950, 3.0)])
    write_csv_gz(trades, cell / 'trades.csv.gz')
    split = oos_subperiods(run_dir, 'AAA/USDT', 8, 200, n_bars=1000,
                            entry_start=650, subperiods=2)
    # the window starts at bar 650 and is cut in two; the trade entered
    # before the window is not part of it
    assert [s['trades'] for s in split['subperiods']] == [2, 2]
    assert split['subperiods'][0]['net_pf'] == pytest.approx(2.0)
    assert split['subperiods'][1]['net_pf'] == pytest.approx(3.0 / 2.0)


def test_the_selection_audit_re_runs_the_family_with_the_runs_own_config(tmp_path):
    """The exact re-runs of the family have to use the audited run's config.

    The family cells of a mutation run are re-run through the real backtest
    to confirm their numbers; with the baseline config the audit would
    confirm the baseline rule and not the child it is auditing.
    """
    from scripts.run_grid import CONFIG_DEFAULTS, load_run_config

    run_dir = tmp_path / 'grid'
    run_dir.mkdir()
    (run_dir / 'run_config.json').write_text(json.dumps({
        'config': dict(CONFIG_DEFAULTS, min_risk_atr=True, atr_threshold=1.0),
    }))
    assert load_run_config(run_dir)['min_risk_atr'] is True

    baseline = Path('results/20261019_135940_grid')
    if (baseline / 'run_config.json').exists():
        assert load_run_config(baseline) == CONFIG_DEFAULTS
