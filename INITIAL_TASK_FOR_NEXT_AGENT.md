# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

**Current state (2026-11-05T02:30:10Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE (~12m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid; unchanged) and `scripts.refresh_gate.gate_status` (eligible=false).
- `universe/last_scan.json` unchanged: state `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, universe_n=275, expansion_floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1 (SUKU rank 1996, mcap $3,231,609), batch_selected=['SUKU/USDT'].
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid coverage in `results/` (`grep -rl SUKU results/` 0 matches) → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.
- Existing wakeup `wku_1a9270d7d001X3kJrIYayNY7kU` due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Do not re-schedule a duplicate.

**What to do:**
1. Re-verify gate eligibility at turn start (compare current UTC time vs `next_eligible_refresh_at` in `universe/last_scan.json`; confirm file unchanged).
2. If still not eligible: record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and wait for the scheduled wakeup / become eligible. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy. Never rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.
