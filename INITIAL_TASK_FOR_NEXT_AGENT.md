# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

**Current state (2026-11-05T04:00:09Z):**
- Gate NOT eligible. `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00` (last refresh 2026-11-05T03:41:37). ~23h 41m remaining. Verified via direct read of `universe/last_scan.json` (26 lines, JSON valid; unchanged vs prior record) and inline Python `datetime.fromisoformat`: bound=`2026-11-06T03:41:37.153817+00:00`, now=`2026-11-05T04:00:19.836463+00:00`, eligible=false, remaining=23:41:17.317354.
- `universe/last_scan.json` unchanged: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` (2000 entries, 20/20 pages, fetched 2026-11-05T03:41:37).
- Expansion floor `PIXEL/USDT` ($3,351,513). Eligible unseen below floor: 0, batch_selected: []. No candidates to apply.
- SUKU has NO fixture and NO grid coverage → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection.
- Wakeup scheduled: `wku_1a9dc2fc40014hhuhGLcmOjc2T` due 2026-11-06T03:46:56Z (5 min after gate opens).

**What to do:**
1. Re-verify gate eligibility at turn start (compare current UTC time vs `next_eligible_refresh_at` in `universe/last_scan.json`).
2. If not eligible: record offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, await wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor/candidates, update `universe/last_scan.json`. Review candidates for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_1a9dc2fc40014hhuhGLcmOjc2T` due 2026-11-06T03:46:56Z. Do not re-schedule a duplicate.