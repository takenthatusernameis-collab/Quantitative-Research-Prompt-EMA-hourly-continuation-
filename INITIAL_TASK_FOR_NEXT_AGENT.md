# Initial Task for Next Agent

## Prior state (2026-11-08T15:36Z — offline gate check; NOT eligible)
- Independent UTC `2026-11-08T15:36:06Z` < `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`). Remaining ≈ 23h53m25s. **No provider calls** made.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` (present), coverage 20/20 pages / 2000 entries / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Coverage guard: `data/fixtures/SUKU_USDT.csv` **ABSENT** — `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. Preserved: `results/FINAL_DECISION.md`, `results/20261019_135940_grid/progress.json`. No candle fetches, no grid reruns, no EMA signal/fill/cost assumption changes.

## Clear initial task
1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC; do not guess. Gate opens **2026-11-09T15:29:31.554859Z**.
2. **If not eligible (expected until gate opens):** make **no provider calls**. Append a brief offline-check record (exact now/bound/remaining, state evidence, SUKU guard status) to `NEXT_AGENT_TASK.md` and this file; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`). Recompute floor vs included-universe fixtures, inspect below-floor band, update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `next_eligible_refresh_at`). Before any `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (`data/fixtures/SUKU_USDT.csv` absent).
4. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling.
