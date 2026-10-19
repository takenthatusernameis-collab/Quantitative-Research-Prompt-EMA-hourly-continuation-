# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- `python -m pytest tests/` → all 16 pass.
- Extended real hourly OHLCV history: BTC/USDT 25,000 rows (~2023-12-12 to 2026-10-19); ETH/SOL/BNB/XRP 22,000 rows (~2024-04-15 to 2026-10-19), UTC, proper OHLCV. `data/fixtures/` + `fetch_manifest.json` updated with real data only.
- Acceptance-command pooled OOS re-run: `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5` → `results/20261019_062434_oos_pooled/`.
  - Pooled: 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.6663.
  - Per-symbol: BTC 124 (PF 0.6860, Sharpe -0.9004); ETH 119 (PF 0.7861, Sharpe -1.8710); SOL 132 (PF 0.8792, Sharpe -1.1395); BNB 150 (PF 0.6955, Sharpe -2.8661); XRP 141 (PF 0.8006, Sharpe -1.8986).

## Robustness variants run (all recorded)
| Variant | Result | Pooled trades | Net PF | Net Sharpe | Max DD |
|---|---|---|---|---|---|
| Baseline (rr=1.5, atr 0.75, OOS 35%) | — | 666 | 0.6890 | -1.9443 | 0.6663 |
| Cost stress 2× (full-sample, `scripts/cost_stress.py`) | base 0.6906 → stress 0.4691; Sharpe 0.8550 → -0.7038; Max DD 1.89 → 4.09 | 1921 | 0.4691 (stress) | -0.7038 (stress) | 4.0922 (stress) |
| stricter_trend (OOS) | identical to baseline — no-op (cross-above-EMA50 in bullish regime already implies close>EMA100; mirror for short) | 666 | 0.6890 | -1.9443 | 0.6663 |
| ATR grid (OOS) | atr 0.5: 826 tr, PF 0.6354, Sharpe -2.1419; atr 1.0: 517 tr, PF 0.6501, Sharpe -2.0586; atr 1.5: 302 tr, PF 0.7922, Sharpe -1.2193 | 302–826 | ≤0.7922 | ≤-1.2193 | — |
| Same-bar exit: conservative SL-first (default) vs aggressive TP-first (`--aggressive-exit`) | conservative 666 tr PF 0.6890 Sharpe -1.9443; aggressive 666 tr PF 0.6952 Sharpe -1.9169 (negligible delta — same-bar conflicts rare) | 666 | 0.6890–0.6952 | -1.9443–-1.9169 | — |

Engineering changes made this cycle:
- `scripts/cost_stress.py`: fixed equity-pooling crash on unequal symbol lengths (now aligns to min length, like `oos_pooled.py`).
- `backtest/backtest.py`: added `conservative_exit` param (default True = SL-first/adverse on same-bar SL&TP conflict).
- `scripts/oos_pooled.py`: added `--aggressive-exit` flag; `conservative_exit` and `aggressive_exit` recorded in config.json.

## Decision label (PROMPT.md §3.4)
**rejected** — fails on OOS net-of-costs (negative Sharpe, PF<1, substantial max drawdown). Larger sample did not improve profitability; cost stress degrades further; no robustness variant reaches profitability. Adequate sample (666 pooled trades, 22k–25k bars/symbol). Do not promote to live trading; do not continue tuning without a new hypothesis (avoid overfitting).

## Next agent task (close-out)
1. Confirm reproducibility: re-run `python -m pytest tests/` (all pass) and re-run the acceptance-command pooled OOS to confirm it reproduces the rejected metrics above.
2. Record the final decision label "rejected" with the rationale above in this handoff (done) and in any final summary artifact.
3. Recommendation: conclude the research — no credible edge found net of costs. No live trading. Further work only with a new, pre-specified hypothesis (not a parameter search on this failed baseline).
4. If completing: mark this handoff complete; no further variants required.

## Acceptance criteria / validation commands
- `python -m pytest tests/` → all pass
- `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5` → `results/*_oos_pooled/summary.json` + `summary.md`, pooled net Sharpe < 0 and net PF < 1 (rejected)
- All robustness variant results recorded above
- Decision label "rejected" recorded
