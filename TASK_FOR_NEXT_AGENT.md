# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-18T11:28:36Z (UTC). Bound: `2026-11-18T12:59:40.659540+00:00`. Gate is **NOT ELIGIBLE** until then (remaining ~1h31m at handoff).

## Your single measurable task

Recompute the gate eligibility offline using `scripts/refresh_gate.py:gate_status` against `universe/last_scan.json` and independent UTC (`date -u` and `datetime.now(timezone.utc)`). Do not guess.

- **If NOT ELIGIBLE (expected):** make **no provider calls**. Append exactly one concise gate-check line (exact now / bound / remaining, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, no pending batch, NUM/GMEE resolved, and the real environment status) to the gate-check log in `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then stop. Do not schedule wakeups (`cron_list` must stay empty).
- **If ELIGIBLE (after 2026-11-18T12:59:40Z):** only take a new provider pass if policy/state requires it. Current state `AWAITING_NEW_ELIGIBLE_CANDIDATES` with `eligible_unseen_below_floor_count=0` means no expansion batch is pending.

## Current state (verified this session)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261117_125940` (scanned_at 2026-11-17T12:59:40.659540Z), `universe_n=278`, expansion floor GMEE/USDT $1,529,405, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `next_eligible_refresh_at=2026-11-18T12:59:40.659540+00:00`.
- Previous batch `["NUM/USDT","GMEE/USDT"]` resolved: fixtures `data/fixtures/NUM_USDT.csv` and `data/fixtures/GMEE_USDT.csv` present (22,001 lines each); grid `results/20261019_135940_grid/progress.json` `completed_cells=18348`, `n_symbols=278` (278x66 complete), NUM/USDT and GMEE/USDT included.
- `universe/mcap_rank.json` n_symbols=278. `results/FINAL_DECISION.md` preserved.

## Environment (re-verified this session)

`python3` 3.12.3 imports only `requests` 2.31.0. `pandas`, `numpy`, `pytest` are **NOT** importable. Gate/scan tooling is stdlib-only and runs; grid/signal/test code cannot run until those packages are reinstalled. Treat as an environment blocker, not a research result.

## Never

Rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.