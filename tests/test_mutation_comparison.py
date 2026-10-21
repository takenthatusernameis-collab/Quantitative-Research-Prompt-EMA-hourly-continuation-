"""Tests for the parent -> child -> delta mutation comparison."""
import gzip
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts.mutation_comparison import (arm_payload, build_verdict,
                                          gate_survivors, scan_grid)

TRADE_COLUMNS = ['bar_index', 'pnl', 'pnl_net', 'entry_cost', 'exit_cost']


def write_cell(run_dir: Path, symbol: str, fast: int, slow: int, trades: list):
    """Write a cell with a trade blotter and a summary."""
    cell_dir = Path(run_dir) / 'results' / symbol.replace('/', '_') / f'P{fast}_{slow}'
    cell_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for index, (bar, gross, entry_cost, exit_cost) in enumerate(trades):
        rows.append({'bar_index': bar, 'pnl': gross,
                     'pnl_net': gross - entry_cost - exit_cost,
                     'entry_cost': entry_cost, 'exit_cost': exit_cost,
                     'risk_pct': 0.01,
                     'symbol': symbol, 'P_fast': fast, 'P_slow': slow})
    frame = pd.DataFrame(rows)
    with gzip.open(cell_dir / 'trades.csv.gz', 'wt', encoding='utf-8') as fh:
        frame.to_csv(fh, index=False)
    (cell_dir / 'summary.json').write_text(json.dumps(
        {'symbol': symbol, 'P_fast': fast, 'P_slow': slow, 'trade_count': len(rows)}))


def write_oos(path: Path, rows: list):
    path.mkdir(parents=True, exist_ok=True)
    with open(path / 'cells.jsonl', 'w') as fh:
        for row in rows:
            fh.write(json.dumps(row) + '\n')


def oos_row(symbol, fast, slow, oos_pf, oos_trades, stress_pf=None):
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'oos_net_pf': oos_pf, 'oos_trades': oos_trades,
            'oos_stress_net_pf': stress_pf if stress_pf is not None else oos_pf}


def test_scan_grid_pools_the_blotters(tmp_path):
    # The symbol has to be a real one: the fold edges come from the length of
    # its hourly fixture, exactly as in the grid-wide legs.
    run_dir = tmp_path / 'grid'
    write_cell(run_dir, 'BTC/USDT', 8, 20, [(1, 10.0, 1.0, 1.0), (2, -4.0, 1.0, 1.0)])
    write_cell(run_dir, 'BTC/USDT', 8, 50, [(1, 5.0, 1.0, 1.0)])
    rows, grid = scan_grid(run_dir, 'data/fixtures', 2, 2.0)
    assert grid['cells'] == 2
    assert grid['trades'] == 3
    # net P&L: (10 - 2) + (-4 - 2) + (5 - 2) = 5
    assert grid['net_pnl'] == pytest.approx(5.0)
    assert grid['net_pf'] == pytest.approx(11.0 / 6.0)
    assert grid['costs'] == pytest.approx(6.0)
    assert len(rows) == 2
    assert all(len(row['folds']) == 2 for row in rows)


def test_gate_survivors_applies_the_three_gates(tmp_path):
    oos_dir = tmp_path / 'oos'
    write_oos(oos_dir, [
        oos_row('A/USDT', 8, 20, 1.4, 50, 1.2),   # clears the gate
        oos_row('B/USDT', 8, 20, 1.4, 10, 1.2),   # too few trades
        oos_row('C/USDT', 8, 20, 1.4, 50, 0.9),   # fails the cost stress
        oos_row('D/USDT', 8, 20, 0.9, 50, 0.9),   # PF below 1
    ])
    survivors = gate_survivors(oos_dir, min_trades=30)
    assert [s['symbol'] for s in survivors] == ['A/USDT']


def test_build_verdict_rejects_a_child_that_does_not_clear_the_gates(tmp_path):
    parent = {'grid_stats': {'net_pf': 0.5, 'gross_pf': 0.9, 'trades': 100,
                              'costs': 10.0, 'cost_share_of_gross_pnl': 0.2,
                              'net_pnl': -1.0, 'cells': 10},
              'walk_forward': {'pooled_oof_net_pf': 0.64,
                               'pooled_oof_stress_net_pf': 0.45,
                               'oof_trades': 1000, 'oof_pf_gt_1': 8},
              'n_gate_survivors': 10, 'n_cells': 100, 'gate_survivors': []}
    child = {'grid_stats': {'net_pf': 0.8, 'gross_pf': 0.9, 'trades': 40,
                             'costs': 5.0, 'cost_share_of_gross_pnl': 0.1,
                             'net_pnl': -1.0, 'cells': 10},
             'walk_forward': {'pooled_oof_net_pf': 0.7,
                              'pooled_oof_stress_net_pf': 0.5,
                              'oof_trades': 400, 'oof_pf_gt_1': 3},
             'n_gate_survivors': 0, 'n_cells': 100, 'gate_survivors': []}
    payload = {'parent': parent, 'child': child, 'decision_rule': 'the rule'}
    verdict = '\n'.join(build_verdict(payload))
    assert 'NOT satisfied' in verdict
    assert 'rejected mutation' in verdict
    # The cost drag really was repaired, and the verdict says so.
    assert 'repairs the cost drag' in verdict
