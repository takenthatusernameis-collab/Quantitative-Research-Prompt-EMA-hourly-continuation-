# Initial Task for Next Agent

## Prior state (2026-11-08T15:29Z — snapshot pass executed, gate now NOT eligible until 2026-11-09T15:29:31Z)
- Gate **ELIGIBLE** at 2026-11-08T15:13:04Z (independent `date -u`) >= `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`. Ran **one** 20-page snapshot pass (no `--apply`): `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`.
- New snapshot `universe/mcap_snapshot_20261108_152931.json`: 2000 entries, pages 20/20, all_requested_pages_returned=true, lowest covered rank 2000 ($3,163,327), `coverage_reaches_below_floor=true`.
- Expansion floor recomputed: **ALPINE/USDT at $3,277,456** (was PIXEL/USDT $3,190,848; PIXEL now excluded/None in fresh snapshot).
- Eligible unseen names below floor: **0** → state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `batch_selected=[]`. No `--apply` run.
- Updated `universe/last_scan.json`: snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json`, scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20/2000/below floor, floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00`.
- Coverage guard: `data/fixtures/SUKU_USDT.csv` **ABSENT** — `--apply` prohibited without verified fixture + baseline grid coverage. Preserved: `results/FINAL_DECISION.md`, `results/20261019_135940_grid/progress.json`. No candle fetches, no grid reruns, no EMA signal/fill/cost assumption changes. Historical research only; no orders.

## Clear initial task
1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC; do not guess. Gate opens **2026-11-09T15:29:31.554859Z**.
2. **If not eligible (expected until gate opens):** make **no provider calls**. Append a brief offline-check record (exact now/bound/remaining, state evidence, SUKU guard status) to `NEXT_AGENT_TASK.md` and this file; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`). Recompute floor vs included-universe fixtures, inspect below-floor band, update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `next_eligible_refresh_at`). Before any `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (`data/fixtures/SUKU_USDT.csv` absent).
4. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling.
