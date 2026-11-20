# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-20T22:10Z (UTC). Bound: `2026-11-21T00:22:43.099527+00:00`. Gate is **NOT ELIGIBLE** until then (~2h12m remaining at handoff).

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

Recompute the gate eligibility offline using `scripts/refresh_gate.py:gate_status` against `universe/last_scan.json` and independent UTC (`date -u` and `datetime.now(timezone.utc)`). Do not guess.

- **If NOT ELIGIBLE (expected before 2026-11-21T00:22:43Z):** make **no provider calls**. Append exactly one concise gate-check row (exact now / bound / remaining, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe 279 / grid 18414, real environment status) to `NEXT_AGENT_TASK.md` §4 and refresh `INITIAL_TASK_FOR_NEXT_AGENT.md`, then stop. Do not schedule wakeups (`cron_list` must stay empty).
- **If ELIGIBLE:** the 24 h pass is due regardless of the stored state. Run exactly one `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`) and record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound.

## Current state (verified 2026-11-20T05:24Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261120_002243` (scanned_at 2026-11-20T00:22:43.099527Z, 25/25 pages, 2500 entries, coverage below floor), `universe_n=279`, expansion floor P2P/USDT $1,455,079, `eligible_unseen_below_floor_count=0`, `batch_selected=["P2P/USDT"]`, `next_eligible_refresh_at=2026-11-21T00:22:43.099527+00:00`.
- Prior batch P2P/USDT resolved: fixture present, grid `results/20261019_135940_grid/progress.json` `completed_cells=18414`, `n_symbols=279`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false` (279×66 complete).
- `universe/mcap_rank.json` n_symbols=279 (updated_at 2026-11-20T00:29:13Z). `data/fixtures` 282 files. `results/FINAL_DECISION.md` preserved. Git tree clean.

## Environment (verified this session)

`python3` 3.12.3 with `requests` 2.31.0 only — pandas/numpy/pytest NOT importable this session, so `scripts/refresh_universe.py plan` fails on `import pandas`. The gate check is stdlib-only and needs no install; re-verify imports at session start and run `python3 -m pip install --user pandas numpy pytest` before any grid/signal/pytest work.

## Never

Rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.
