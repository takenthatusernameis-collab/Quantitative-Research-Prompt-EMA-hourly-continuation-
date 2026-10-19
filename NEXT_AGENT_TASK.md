# NEXT AGENT TASK

## Status
- Tests: 16/16 passed (confirmed). `python -m pytest tests/` ✓
- Acceptance OOS (reproduced): `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5`
  - Results dir: `results/20261019_064215_oos_pooled/`
  - Pooled: 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663
  - Per-symbol: BTC 124 (PF 0.6860, Sharpe -0.9004); ETH 119 (PF 0.7861, Sharpe -1.8710); SOL 132 (PF 0.8792, Sharpe -1.1395); BNB 150 (PF 0.6955, Sharpe -2.8661); XRP 141 (PF 0.8006, Sharpe -1.8986)

## Robustness variants recorded
| Variant | Result | Pooled trades | Net PF | Net Sharpe | Max DD |
|---|---|---|---|---|---|
| Baseline (rr=1.5, atr 0.75, OOS 35%) | — | 666 | 0.6890 | -1.9443 | 0.6663 |
| Cost stress 2× (full-sample, `scripts/cost_stress.py`) | base 0.6906 → stress 0.4691; Sharpe 0.8550 → -0.7038; Max DD 1.89 → 4.09 | 1921 | 0.4691 (stress) | -0.7038 (stress) | 4.0922 (stress) |
| stricter_trend (OOS) | identical to baseline — no-op (cross-above-EMA50 in bullish regime already implies close>EMA100; mirror for short) | 666 | 0.6890 | -1.9443 | 0.6663 |
| ATR grid (OOS) | atr 0.5: 826 tr, PF 0.6354, Sharpe -2.1419; atr 1.0: 517 tr, PF 0.6501, Sharpe -2.0586; atr 1.5: 302 tr, PF 0.7922, Sharpe -1.2193 | 302–826 | ≤0.7922 | ≤-1.2193 | — |
| Same-bar exit: conservative SL-first (default) vs aggressive TP-first (`--aggressive-exit`) | conservative 666 tr PF 0.6890 Sharpe -1.9443; aggressive 666 tr PF 0.6952 Sharpe -1.9169 (negligible delta) | 666 | 0.6890–0.6952 | -1.9443–-1.9169 | — |

## Engineering changes
- `scripts/cost_stress.py`: fixed equity-pooling crash on unequal symbol lengths (aligns to min length).
- `backtest/backtest.py`: added `conservative_exit` param (default True = SL-first/adverse on same-bar SL&TP conflict).
- `scripts/oos_pooled.py`: added `--aggressive-exit` flag; records conservative_exit/aggressive_exit in config.json.

## Decision
**rejected** — fails on OOS net-of-costs (negative Sharpe, PF<1, substantial max drawdown). Larger real sample did not improve profitability; cost stress degrades further; no robustness variant reaches profitability. Adequate sample (666 pooled trades, 22k–25k bars/symbol). Do not promote to live trading. Further work only with a new, pre-specified hypothesis (not parameter search on this baseline).

## Next agent task
1. Read this handoff and confirm environment is clean; re-run quick sanity if desired (`python -m pytest tests/`).
2. Conclude research formally: document final decision in a concise summary artifact at `results/FINAL_DECISION.md` (include pooled metrics, rationale, robustness summary, and "no live trading; new hypothesis required").
3. Ensure all results, configs, and manifests are consistent and committed state is clean (no unstaged test data changes required; data is tracked).
4. Report completion by updating this handoff to "CLOSED" with final outcome. No further variants required.

## Acceptance criteria
- `python -m pytest tests/` → 16/16 pass
- `results/FINAL_DECISION.md` exists with required content
- Decision "rejected" clearly recorded with rationale
- Handoff marked CLOSED


## CLOSED
- Confirmed tests pass (16/16). Reproduced acceptance OOS; metrics match (666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663).
- Created `results/FINAL_DECISION.md` with decision, rationale, robustness, and recommendation.
- Decision: **rejected**. No live trading. New hypothesis required for further work.
