# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

**Current state (2026-11-05T03:50:25Z):**
- Gate eligible. `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00` (last refresh at `2026-11-05T03:41:37.153817+00:00`).
- `universe/last_scan.json` updated to state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137.json` (2000 entries, 20/20 pages, fetched 2026-11-05T03:41:37.153817+00:00).
- Expansion floor moved to `PIXEL/USDT` ($3,351,513). Eligible unseen below floor: 0, batch_selected: []. No candidates to apply.
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid coverage in `results/` (`grep -rl SUKU results/` exit=1) → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. Git tree clean except modified `universe/last_scan.json` and untracked snapshot file.
- Next refresh eligible at `2026-11-06T03:41:37.153817+00:00` (~23h51m from now).

**What to do:**
1. Re-verify gate eligibility at turn start (compare current UTC time vs `next_eligible_refresh_at` in `universe/last_scan.json`; confirm file state).
2. If not eligible: record offline check in `NEXT_AGENT_TASK.md`, ensure appropriate wakeup if needed, wait. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor/candidates, update `universe/last_scan.json` via `--apply-from` or normal flow. Review candidates for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy. Never rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.
