# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, and `universe/last_scan.json` before acting.

## Current state (re-verified 2026-11-08T15:54Z, offline)
- `universe/last_scan.json`: state=`AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` (present, 543610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- `next_eligible_refresh_at` = `2026-11-09T15:29:31.554859+00:00`. **NOT ELIGIBLE** at `2026-11-08T15:54:11Z` (independent `date -u`/Python UTC): remaining ≈ 23h35m20s (84920s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed.
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3163327, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={ALPINE/USDT, $3,277,456}, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` **ABSENT** (no `*suku*` matches). **`--apply` MUST NOT run** without verified fixture + baseline grid coverage for every selected candidate.
- Preserved artifacts: `results/FINAL_DECISION.md` (23304 bytes; program-level rejection, 0 credible candidates), `results/20261019_135940_grid/progress.json` (1478918 bytes; 18,150 cells, 0 blocked). EMA signal/fill/cost assumptions unchanged.

## Clear initial task for next agent
1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC; do not guess. Gate opens **2026-11-09T15:29:31.554859Z**.
2. **If not eligible (expected until gate opens):** make **no provider calls**. Append a brief offline-check record (exact now/bound/remaining, state evidence, SUKU guard status) to `NEXT_AGENT_TASK.md` and this file; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`). Recompute floor vs included-universe fixtures, inspect below-floor band, update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `next_eligible_refresh_at`). Before any `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (`data/fixtures/SUKU_USDT.csv` absent).
4. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow `AGENTS.md` adaptive gate policy.
