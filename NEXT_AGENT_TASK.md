# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass.
- Threshold sweep (0.7/0.75/0.8) completed; 0.75 best (36 trades, net PF 0.4257, Sharpe -7.99).
- Walk-forward/OOS attempted; test windows produced 0 trades (too sparse/short). stricter_trend no effect.
- Summary: results/robustness_summary.md

## Next agent task
1. Run pooled cross-symbol OOS with larger test windows (e.g., 30-40% split) and per-symbol OOS aggregation; report metrics.
2. Investigate signal sparsity in short windows; consider minimum history and warmup handling.
3. Test stricter_trend combined with threshold variations if beneficial.
4. Update handoff with findings.
