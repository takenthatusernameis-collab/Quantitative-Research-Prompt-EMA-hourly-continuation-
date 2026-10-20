"""Tests for the candidate-check harness (OOS + cost stress gates)."""
import json
import sys

import pandas as pd

from scripts import candidate_check
from scripts.candidate_check import load_candidates, load_completed_rows, verdict


def _legs(base_pf=1.2, base_sh=0.5, oos_pf=1.1, oos_sh=0.2, oos_n=100,
          stress_pf=1.05, stress_oos_pf=1.02):
    return {
        'base': {'metrics': {'net_profit_factor': base_pf, 'sharpe_ratio': base_sh}},
        'oos': {'metrics': {'net_profit_factor': oos_pf, 'sharpe_ratio': oos_sh,
                            'trade_count': oos_n}},
        'stress': {'metrics': {'net_profit_factor': stress_pf}},
        'stress_oos': {'metrics': {'net_profit_factor': stress_oos_pf}},
    }


def test_verdict_credible_requires_all_gates():
    """All four gates green -> credible candidate (PROMPT.md §3.4)."""
    assert verdict(_legs()) == 'credible candidate'


def test_verdict_is_exploratory_when_cost_stress_breaks_the_edge():
    """An OOS edge that fails cost stress is exploratory, not credible."""
    assert verdict(_legs(stress_pf=0.9)) == 'exploratory signal'


def test_verdict_is_exploratory_when_oos_cost_stress_breaks_the_edge():
    """The cost-stress gate also applies to the out-of-sample window."""
    assert verdict(_legs(stress_oos_pf=0.8)) == 'exploratory signal'


def test_verdict_rejects_when_oos_fails():
    """An in-sample edge that dies out of sample is not a candidate."""
    assert verdict(_legs(oos_pf=0.91, oos_sh=-0.5)) == 'rejected'


def test_verdict_rejects_when_oos_trade_count_is_too_small():
    """Too few OOS trades means no statistical power."""
    assert verdict(_legs(oos_n=10)) == 'rejected'


def test_verdict_exploratory_when_only_oos_gate_fails():
    """OOS edge without the robustness gate is exploratory, not credible."""
    assert verdict(_legs(oos_pf=1.1, oos_sh=0.2, stress_pf=0.9)) == 'exploratory signal'


def test_verdict_rejects_when_oos_pf_is_below_one():
    """The JASMY/USDT case: in-sample PF > 1, OOS PF < 1 -> rejected."""
    assert verdict(_legs(oos_pf=0.9068, oos_sh=-0.59, oos_n=174)) == 'rejected'


def test_load_candidates_parses_explicit_cell_list(tmp_path):
    """The --cells syntax is SYMBOL/USDT:fast:slow (comma separated)."""
    cells = load_candidates(tmp_path, 'JASMY/USDT:20:200,JASMY/USDT:21:200')
    assert cells == [('JASMY/USDT', 20, 200), ('JASMY/USDT', 21, 200)]


def test_load_candidates_discovers_cells_above_one_pf(tmp_path):
    """Without --cells, every cell with net PF > 1 is picked up."""
    run_dir = tmp_path / 'grid'
    cell = run_dir / 'results' / 'JASMY_USDT' / 'P20_200'
    cell.mkdir(parents=True)
    (cell / 'summary.json').write_text(
        '{"P_fast": 20, "P_slow": 200, "net_profit_factor": 1.01}')
    other = run_dir / 'results' / 'BTC_USDT' / 'P20_200'
    other.mkdir(parents=True)
    (other / 'summary.json').write_text(
        '{"P_fast": 20, "P_slow": 200, "net_profit_factor": 0.5}')
    assert load_candidates(run_dir, None) == [('JASMY/USDT', 20, 200)]


def test_load_completed_rows_ignores_a_truncated_line(tmp_path):
    """An interrupted run leaves a partial last line; it must not break resume."""
    path = tmp_path / 'rows.jsonl'
    row = {'symbol': 'AAA/USDT', 'P_fast': 8, 'P_slow': 12, 'decision_label': 'rejected'}
    path.write_text(json.dumps(row) + '\n' + '{"symbol": "BBB/UDT')
    done = load_completed_rows(path)
    assert list(done) == [('AAA/USDT', 8, 12)]


def test_candidate_check_reuses_computed_cells(tmp_path, monkeypatch):
    """A cell already computed in an interrupted run is not recomputed."""
    out = tmp_path / 'check'
    out.mkdir()
    row = {'symbol': 'AAA/USDT', 'P_fast': 8, 'P_slow': 12,
           'decision_label': 'rejected',
           'legs': {'base': {'net_profit_factor': 1.0, 'sharpe_ratio': 0.0},
                    'oos': {'net_profit_factor': 0.0, 'sharpe_ratio': 0.0, 'trade_count': 0},
                    'stress': {'net_profit_factor': 1.0},
                    'stress_oos': {'net_profit_factor': 0.0}}}
    (out / 'rows.jsonl').write_text(json.dumps(row) + '\n')

    calls = []

    def fake_run_cell(*args, **kwargs):
        calls.append(args[:3])
        return pd.DataFrame(), pd.DataFrame(), {'net_profit_factor': 0.0,
                                                'sharpe_ratio': 0.0, 'trade_count': 0}

    monkeypatch.setattr(candidate_check, 'load_candidates',
                        lambda run_dir, explicit: [('AAA/USDT', 8, 12)])
    monkeypatch.setattr(candidate_check, 'run_cell', fake_run_cell)
    monkeypatch.setattr(candidate_check, 'load_ohlcv_csv', lambda path: pd.DataFrame({'close': [1.0]}))
    monkeypatch.setattr(sys, 'argv', ['candidate_check.py', '--run', str(tmp_path / 'grid'),
                                      '--out', str(out)])

    candidate_check.main()

    assert calls == []
    summary = json.loads((out / 'summary.json').read_text())
    assert [c['symbol'] for c in summary['cells']] == ['AAA/USDT']
