# EMA mutation metadata reconciliation — 30 October 2026

The `C_min_risk_atr` entry in `results/mutations.json` was inconsistent with the execution manifest.

Verified source of truth: `results/20261021_172619_grid/run_config.json`:

- Run ID: `20261021_172619_grid`
- `stricter_trend`: false
- `min_risk_atr`: true

The summary ledger had instead pointed to `20261022_134500_grid` and recorded `stricter_trend=true`, `min_risk_atr=false`. That configuration belongs to the separate stricter-trend run.

The correction changes metadata only. All stored results, metrics, candidate decisions, and experiment artifacts remain unchanged. No grid was rerun and no holdout was opened.
