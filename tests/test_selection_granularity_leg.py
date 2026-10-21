"""Tests for the selection-granularity leg."""
import math

import numpy as np
import pandas as pd
import pytest

from scripts.run_grid import write_csv_gz
from scripts.selection_granularity_leg import (collect_grid_folds, family_walk_forward,
                                               merge_pair_folds, percentile_of,
                                               random_walk_forward_steps)


def fold(index, trades, win, loss, stress_win=None, stress_loss=None):
    """One fold of fold statistics."""
    return {'fold': index, 'trades': trades, 'win_sum': win, 'loss_abs': loss,
            'stress_win_sum': stress_win if stress_win is not None else win,
            'stress_loss_abs': stress_loss if stress_loss is not None else loss}


def cell(symbol, fast, slow, folds):
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow, 'folds': folds}


def test_merge_pair_folds_pools_the_symbols_of_a_family():
    cells = [
        cell('AAA/USDT', 8, 200, [fold(0, 2, 10.0, 1.0), fold(1, 1, 5.0, 1.0)]),
        cell('BBB/USDT', 8, 200, [fold(0, 3, 6.0, 2.0), fold(1, 2, 4.0, 1.0)]),
        cell('AAA/USDT', 20, 200, [fold(0, 1, 1.0, 1.0), fold(1, 1, 1.0, 1.0)]),
    ]
    merged = merge_pair_folds(cells, 2)
    assert set(merged) == {(8, 200), (20, 200)}
    assert merged[(8, 200)][0]['trades'] == 5
    assert merged[(8, 200)][0]['win_sum'] == pytest.approx(16.0)
    assert merged[(8, 200)][0]['loss_abs'] == pytest.approx(3.0)
    assert merged[(8, 200)][1]['trades'] == 3


def test_family_walk_forward_scores_the_selection_on_an_unseen_fold():
    # Pair 8/200 is the better one on the history, pair 20/200 is the better
    # one on the fold the selection never saw.
    cells = [
        cell('AAA/USDT', 8, 200, [fold(0, 30, 60.0, 10.0), fold(1, 10, 1.0, 9.0)]),
        cell('AAA/USDT', 20, 200, [fold(0, 30, 40.0, 20.0), fold(1, 10, 20.0, 1.0)]),
    ]
    steps = family_walk_forward(cells, 2, min_history_trades=20)
    assert len(steps) == 1
    step = steps[0]
    assert step['selected'] == (8, 200)
    assert step['oof_trades'] == 10
    assert step['oof_net_pf'] == pytest.approx(1.0 / 9.0)


def test_family_walk_forward_skips_a_pair_without_enough_history():
    cells = [cell('AAA/USDT', 8, 200, [fold(0, 3, 60.0, 1.0), fold(1, 10, 1.0, 9.0)])]
    steps = family_walk_forward(cells, 2, min_history_trades=20)
    assert steps[0]['selected'] is None


def test_family_walk_forward_pools_the_trades_of_the_family():
    cells = [
        cell('AAA/USDT', 8, 200, [fold(0, 20, 30.0, 10.0), fold(1, 4, 2.0, 2.0)]),
        cell('BBB/USDT', 8, 200, [fold(0, 20, 10.0, 10.0), fold(1, 6, 3.0, 3.0)]),
    ]
    steps = family_walk_forward(cells, 2, min_history_trades=20)
    step = steps[0]
    # the history is the pooled fold 0 of both symbols, the test fold is the
    # pooled fold 1
    assert step['history_trades'] == 40
    assert step['history_net_pf'] == pytest.approx(40.0 / 20.0)
    assert step['oof_trades'] == 10
    assert step['oof_net_pf'] == pytest.approx(5.0 / 5.0)


def test_random_walk_forward_picks_an_eligible_cell_and_scores_it():
    cells = [
        cell('AAA/USDT', 8, 200, [fold(0, 30, 60.0, 10.0), fold(1, 10, 1.0, 9.0)]),
        cell('AAA/USDT', 20, 200, [fold(0, 30, 40.0, 20.0), fold(1, 10, 20.0, 1.0)]),
    ]
    rng = np.random.default_rng(7)
    picks = set()
    for _ in range(40):
        steps = random_walk_forward_steps(cells, 2, 20, rng)
        assert steps[0]['selected'] in {(8, 200), (20, 200)}
        assert steps[0]['oof_trades'] == 10
        picks.add(steps[0]['selected'])
    # the control really is random: both cells show up
    assert picks == {(8, 200), (20, 200)}


def test_random_walk_forward_is_reproducible_for_a_seed():
    cells = [
        cell('AAA/USDT', 8, 200, [fold(0, 30, 60.0, 10.0), fold(1, 10, 1.0, 9.0)]),
        cell('AAA/USDT', 20, 200, [fold(0, 30, 40.0, 20.0), fold(1, 10, 20.0, 1.0)]),
    ]
    first = [random_walk_forward_steps(cells, 2, 20, np.random.default_rng(11))[0]['selected']
             for _ in range(10)]
    second = [random_walk_forward_steps(cells, 2, 20, np.random.default_rng(11))[0]['selected']
              for _ in range(10)]
    assert first == second


def test_random_walk_forward_has_no_selection_without_history():
    cells = [cell('AAA/USDT', 8, 200, [fold(0, 3, 60.0, 1.0), fold(1, 10, 1.0, 9.0)])]
    steps = random_walk_forward_steps(cells, 2, 20, np.random.default_rng(3))
    assert steps[0]['selected'] is None


def test_percentile_of_the_random_draws():
    draws = [0.4, 0.5, 0.6, 0.7]
    assert percentile_of(0.6, draws) == pytest.approx(0.75)
    assert percentile_of(0.1, draws) == pytest.approx(0.0)
    assert percentile_of(0.9, draws) == pytest.approx(1.0)
    assert percentile_of(None, draws) is None


def test_collect_grid_folds_reads_the_blotters_of_a_run(tmp_path):
    fixture_dir = tmp_path / 'fixtures'
    fixture_dir.mkdir()
    bars = 100
    with open(fixture_dir / 'AAA_USDT.csv', 'w') as fh:
        fh.write('timestamp,open,high,low,close,volume\n')
        for i in range(bars):
            fh.write(f'2024-01-01 00:{i:02d}:00+00:00,1,1,1,1,1\n')
    cell_dir = tmp_path / 'results' / 'AAA_USDT' / 'P8_200'
    cell_dir.mkdir(parents=True)
    trades = pd.DataFrame([
        {'bar_index': 0, 'pnl': 10.0, 'pnl_net': 10.0, 'entry_cost': 0.0, 'exit_cost': 0.0},
        {'bar_index': 60, 'pnl': -4.0, 'pnl_net': -4.0, 'entry_cost': 0.0, 'exit_cost': 0.0},
        {'bar_index': 90, 'pnl': 6.0, 'pnl_net': 6.0, 'entry_cost': 0.0, 'exit_cost': 0.0},
    ])
    write_csv_gz(trades, cell_dir / 'trades.csv.gz')
    rows = collect_grid_folds(tmp_path, ['AAA/USDT'], str(fixture_dir), 2)
    assert len(rows) == 1
    assert rows[0]['n_bars'] == bars
    # the two folds split the 100 bars in half
    assert [f['trades'] for f in rows[0]['folds']] == [1, 2]
