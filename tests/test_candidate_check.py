"""Tests for the candidate-check harness (OOS + cost stress gates)."""
from scripts.candidate_check import load_candidates, verdict


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
