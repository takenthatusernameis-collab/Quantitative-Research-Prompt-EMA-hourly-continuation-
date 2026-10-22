**Session 2026-10-22T04:45Z (follow-on).** Read `NEXT_AGENT_TASK.md` first, then `results/mutations.json` (C_min_risk_atr: NOT_PROMOTED) and `universe/last_scan.json`.

**State.**
- ATR min-risk mutation is closed as `NOT_PROMOTED`; all decision legs complete. Baseline grid `results/20261019_135940_grid` (266 symbols × 66 pairs = 17 556 cells) remains the program's grid. Child `results/20261021_172619_grid` kept as a documented reproducible negative result.
- Universe N=266, floor AGLD/USDT $16 279 472, snapshot `universe/mcap_snapshot_20261021_114120.json` (scanned 2026-10-21T11:41:20Z). Next eligible refresh: **2026-10-22T11:41:20Z**.
- Tests: `198 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T04:39Z). Env: numpy 2.5.4, pandas 3.0.6, pytest 9.1.1 in user site-packages.

**Constraints.**
- Do **not** contact the market-data provider before 2026-10-22T11:41:20Z (no polling/checks). After that timestamp: **exactly one** fetch allowed; freeze the new snapshot for the following 24 h.
- Do **not** re-run the baseline grid, do **not** re-open the child grid, do **not** start a second worker on any run directory, do **not** promote anything from the child grid.

**Next task (time-gated).**
From 2026-10-22T11:41:20Z onward:
1. Perform exactly one universe fetch (CoinGecko /api/v3/coins/markets as before), save snapshot to `universe/mcap_snapshot_YYYYMMDD_HHMMSS.json`, update `universe/last_scan.json` (coverage, `next_eligible_refresh_at = scanned_at + 24h`, `state`, etc.).
2. Apply §2.1 expansion procedure to **new symbols only** (respect exclusions: insufficient hourly history for grid / no tradable KuCoin spot USDT pair). Fetch KuCoin hourly fixtures for new names as needed.
3. Expand the grid by running `scripts/run_grid.py` with `--resume` one symbol at a time in descending market-cap order against the baseline config. Do not disturb existing cells.
4. After expansion, update `universe/last_scan.json` to reflect new `universe_n`, snapshot linkage, and verification note. If no eligible new symbols, record that clearly and return to `AWAITING_NEW_ELIGIBLE_CANDIDATES` with next refresh 24 h out.

**If starting a new mutation:** run the full corrected pipeline with child's own null as yardstick: `run_mutation_grid.py --resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` → `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan`. Run `PYTHONPATH=. python3 -m pytest tests/ -q` after any code change.
