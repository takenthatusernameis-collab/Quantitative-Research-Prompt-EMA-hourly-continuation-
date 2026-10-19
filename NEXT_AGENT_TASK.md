# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass (`python -m pytest tests/`).
- Obtained longer real hourly OHLCV history: BTC/USDT extended to 25,000 rows (~2023-12-12 to 2026-10-19); ETH/SOL/BNB/XRP at 15,000 rows (~2025-02-01 to 2026-10-19) with UTC timestamps and proper OHLCV columns. Data files updated in `data/fixtures/` with `fetch_manifest.json` documenting source, interval, timezone, spans.
- Pooled cross-symbol OOS with 35% test windows + per-symbol OOS aggregation: `results/20261019_055612_oos_pooled/`.
  - Pooled: 498 trades, net PF 0.6882, net WR 0.3956, net Sharpe -2.2615, max DD 0.4490 (5 symbols, market-cap desc).
  - Per-symbol: BTC 124 trades (PF 0.6860, Sharpe -0.9004); ETH 82 (PF 0.8853, Sharpe -1.4806); SOL 93 (PF 0.6122, Sharpe -3.1277); BNB 107 (PF 0.5788, Sharpe -4.3132); XRP 92 (PF 0.6780, Sharpe -2.8792).
- Signal sparsity remains a constraint for symbols with shorter history (~5250 test bars effective) despite larger BTC window; 100-bar EMA warmup further shrinks effective OOS.
- Summary updated: `results/robustness_summary.md` and `results/validation_real_data.json` (created earlier) reflect current state.
- Decision label (PROMPT.md §3.4): **rejected** on OOS with net costs (negative Sharpe, PF<1, substantial max DD). Even with longer BTC history, pooled OOS is not profitable net-of-costs under the baseline specification.

## Next agent task
1. **Improve data coverage:** extend remaining symbols (ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT) to comparable multi-year history (≥20k hourly bars) so test windows are statistically meaningful across all symbols. Document any API limits and update `data/fixtures/` with real data only (no synthesis/fill). Update `fetch_manifest.json` and timezone documentation.
2. **Explore robustness:** run controlled mutations (cost stress 2×, stricter_trend, atr_threshold grid, conservative same-bar exit assumption) on the longer-history pooled OOS to see if any variant becomes net-profitable. Prefer running via existing scripts (`scripts/cost_stress.py`, pooled runner with flags).
3. **Consider alternative specifications** only if robustness tests consistently fail but sample is adequate: e.g. adjust RR/filtering or test a different continuation definition, but do NOT overfit. Document all tested variants with trade counts.
4. Re-run pooled cross-symbol OOS on the final dataset and report pooled + per-symbol metrics with a clear decision label (credible candidate / exploratory signal / rejected / blocked).

## Acceptance criteria / validation commands
- `python -m pytest tests/` → all pass
- Update fixtures + `fetch_manifest.json` with real, documented hourly data (UTC) for all 5 symbols with sufficient history for 35% OOS windows
- `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5` → produces `results/*_oos_pooled/summary.json` and `summary.md` with pooled + per-symbol metrics
- Run at least one robustness variant (e.g. `PYTHONPATH=. python scripts/cost_stress.py ...`) and record results
- Handoff (`NEXT_AGENT_TASK.md`) updated with new findings, all variant results, and decision label
