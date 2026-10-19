# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass (`python -m pytest tests/`).
- Extended real hourly OHLCV history: BTC/USDT 25,000 rows (~2023-12-12 to 2026-10-19); ETH/SOL/BNB/XRP 22,000 rows (~2024-04-15 to 2026-10-19), UTC, proper OHLCV. `data/fixtures/` + `fetch_manifest.json` updated with real data only.
- Pooled cross-symbol OOS 35% test windows: `results/20261019_062302_oos_pooled/`.
  - Pooled: 666 trades, net PF 0.6890, net Sharpe -1.9443, max DD 0.4490 (5 symbols).
  - Per-symbol: BTC 124 (PF 0.6860, Sharpe -0.9004); ETH 119 (PF 0.7861, Sharpe -1.8710); SOL 132 (PF 0.8792, Sharpe -1.1395); BNB 150 (PF 0.6955, Sharpe -2.8661); XRP 141 (PF 0.8006, Sharpe -1.8986).
- Decision label (PROMPT.md §3.4): **rejected** on OOS net-of-costs (negative Sharpe, PF<1, substantial max DD). Larger sample did not improve profitability.

## Next agent task
1. Run robustness variants on pooled OOS: cost stress 2×, stricter_trend, atr_threshold grid, conservative same-bar exit. Use `scripts/cost_stress.py` and pooled runner flags. Record trade counts + metrics.
2. If all variants fail with adequate sample, explore alternative specifications (RR/filtering/continuation definition) without overfitting; document.
3. Re-run pooled OOS on final dataset and report pooled + per-symbol metrics with decision label.
4. Update this handoff with variant results and decision label.

## Acceptance criteria / validation commands
- `python -m pytest tests/` → all pass
- `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5` → `results/*_oos_pooled/summary.json` + `summary.md`
- At least one robustness variant run and recorded
- Handoff updated with findings + decision label
