# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-21T22:27Z (UTC). Bound: `2026-11-22T03:13:02.267371+00:00`. Gate is **AWAITING_NEW_ELIGIBLE_CANDIDATES** (NOT ELIGIBLE) until then (~4h45m remaining at handoff; last check 2026-11-21T22:27:55Z, remaining 4h45m06s / 17,106s). The prior bound `2026-11-21T00:22:43.099527+00:00` elapsed and the due 24 h ranking pass was taken and fully applied (batch HTR/USDT → universe 280 / grid 18480).

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

Recompute the gate eligibility offline using `scripts/refresh_gate.py:gate_status` against `universe/last_scan.json` and independent UTC (`date -u` and `datetime.now(timezone.utc)`). Do not guess.

- **If NOT ELIGIBLE (expected before 2026-11-22T03:13:02Z):** make **no provider calls**. Append exactly one concise gate-check row (exact now / bound / remaining, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe 280 / grid 18480, real environment status) to `NEXT_AGENT_TASK.md` §4 and refresh `INITIAL_TASK_FOR_NEXT_AGENT.md`, then stop. Do not schedule wakeups (`cron_list` must stay empty).
- **If ELIGIBLE:** the 24 h pass is due. Run exactly one `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`) and record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound.

## Current state (verified 2026-11-21T22:27Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261121_031302` (scanned_at 2026-11-21T03:13:02.267371Z, 25/25 pages, 2500 entries, coverage below floor), `universe_n=280`, expansion floor HTR/USDT $1,403,310, `eligible_unseen_below_floor_count=0`, `batch_selected=["HTR/USDT"]`, `next_eligible_refresh_at=2026-11-22T03:13:02.267371+00:00`.
- Prior batch HTR/USDT resolved: fixture `data/fixtures/HTR_USDT.csv` present (22000 rows, all integrity checks OK), grid `results/20261019_135940_grid/progress.json` `completed_cells=18480`, `n_symbols=280`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false` (280×66 complete). Batch 34 appended to `universe/mcap_expansion_log.md`.
- `universe/mcap_rank.json` n_symbols=280 (last 3: GMEE/USDT, P2P/USDT, HTR/USDT). `data/fixtures` 283 files incl. `HTR_USDT.csv`. `results/FINAL_DECISION.md` preserved. Git tree clean.

## Environment (verified this session)

`python3` 3.12.3 with `requests 2.31.0` importable. **pandas/numpy/pytest are NOT importable
this session** (`ModuleNotFoundError`); reinstall them (free PyPI) before any grid/signal work
that needs pandas. The gate check is stdlib-only and needs no install.

## Never

Rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.
