# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

**Current state (2026-11-05T03:51:39Z):**
- Gate NOT eligible. `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00` (last refresh 2026-11-05T03:41:37). ~23h50m remaining.
- `universe/last_scan.json` state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137.json` (2000 entries, 20/20 pages, fetched 2026-11-05T03:41:37).
- Expansion floor `PIXEL/USDT` ($3,351,513). Eligible unseen below floor: 0, batch_selected: []. No candidates to apply.
- SUKU has NO fixture and NO grid coverage → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection.
- Wakeup scheduled: `wku_1a9d5b043001H8BIEfnC7cyhv8` due 2026-11-06T03:46:56Z.

**What to do:**
1. Re-verify gate eligibility at turn start (compare current UTC time vs `next_eligible_refresh_at`).
2. If not eligible: record offline check in `NEXT_AGENT_TASK.md`, await wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor/candidates, update `universe/last_scan.json`. Review candidates for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy. Never rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.
