# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass (`python -m pytest tests/`).
- Pooled cross-symbol OOS with 35% test windows + per-symbol OOS aggregation: `results/20261019_015325_oos_pooled/`.
  - Pooled: 19 trades, net PF 0.2175, net WR 0.316, net Sharpe -13.29, max DD 0.0009 (5 symbols, market-cap desc).
  - Per-symbol: BTC 0 trades; ETH 3 (PF 0.2264); SOL 4 (PF 0.2124); BNB 4 (PF 0.1804); XRP 8 (PF 0.5869).
- Signal sparsity: only 4-15 qualifying signals per ~175-bar test window; 100-bar EMA warmup shrinks effective OOS sample further.
- stricter_trend: no effect (identical metrics to base). atr_threshold 0.80 vs 0.75: no meaningful benefit (18 trades, PF 0.2176).
- Summary: `results/robustness_summary.md` + `results/validation_real_data.json`.
- Decision label (PROMPT.md §3.4): **rejected** on OOS (negative Sharpe, low trade count, fails costs). Binding constraint is DATA — fixtures are only ~21 days (500 bars/symbol).

## Next agent task
1. **Obtain/fix data:** source longer hourly OHLCV history for the top-N market-cap crypto symbols (current universe: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT in `universe/mcap_rank.json`). Target: months-to-years of hourly bars per symbol so a 30-40% OOS window has statistical power. Do NOT synthesize/fill data.
2. Update `data/fixtures/` with real (or clearly documented fixture) hourly CSVs: columns `timestamp, open, high, low, close, volume`; timezone documented.
3. Re-run pooled cross-symbol OOS (`scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5`) on the longer history and report pooled + per-symbol metrics.
4. Re-assess decision label (credible candidate / exploratory signal / rejected / blocked) and update this handoff with findings.

## Acceptance criteria / validation commands
- `python -m pytest tests/` → all pass
- `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5` → produces `results/*_oos_pooled/summary.json` and `summary.md` with pooled + per-symbol metrics
- Handoff (`NEXT_AGENT_TASK.md`) updated with new findings and decision label

(End of file)
