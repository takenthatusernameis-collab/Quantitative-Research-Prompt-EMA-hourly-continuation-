# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-19T01:17:58Z (UTC). Bound: `2026-11-19T19:50:23.792771+00:00`. Gate is **NOT ELIGIBLE** until then (~18h32m remaining at handoff).

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

Recompute the gate eligibility offline using `scripts/refresh_gate.py:gate_status` against `universe/last_scan.json` and independent UTC (`date -u` and `datetime.now(timezone.utc)`). Do not guess.

- **If NOT ELIGIBLE (expected before 2026-11-19T19:50:23Z):** make **no provider calls**. Append exactly one concise gate-check row (exact now / bound / remaining, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe 278 / grid 18348, real environment status) to `NEXT_AGENT_TASK.md` §4 and refresh `INITIAL_TASK_FOR_NEXT_AGENT.md`, then stop. Do not schedule wakeups (`cron_list` must stay empty).
- **If ELIGIBLE:** the 24 h pass is due regardless of the stored state. Run exactly one `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`) and record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound.

## Current state (verified 2026-11-19T01:17:58Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261118_195023` (scanned_at 2026-11-18T19:50:23.792771Z, 25/25 pages, 2500 entries, coverage below floor), `universe_n=278`, expansion floor CERE/USDT $1,528,741, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `next_eligible_refresh_at=2026-11-19T19:50:23.792771+00:00`.
- Prior batch NUM/USDT + GMEE/USDT resolved: fixtures present (22,001 lines each), grid `results/20261019_135940_grid/progress.json` `completed_cells=18348`, `n_symbols=278` (278×66 complete), both symbols included.
- `universe/mcap_rank.json` n_symbols=278. `results/FINAL_DECISION.md` preserved.

## Environment (verified this session)

`python3` 3.12.3 with pandas 3.1.1, numpy 2.5.5, pytest 9.2.0, requests 2.31.0, installed `--user` under a temporary home. Re-check imports at session start; if missing, run `python3 -m pip install --user pandas numpy pytest`. Gate/scan tooling is stdlib-only.

## Never

Rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.
