# Initial Task for Next Agent

**Task:** Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-03T18:46:47Z):**
- Gate `next_eligible_refresh_at` = `2026-11-04T01:35:03.192568+00:00`. NOT ELIGIBLE at handoff time (~6h48m15s remaining; re-verify at resume).
- `universe/last_scan.json`: state `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261103_013503`, scanned_at `2026-11-03T01:35:03.192568+00:00`, coverage 20/20 pages, 2000 entries, universe_n=275, expansion floor `ALPINE/USDT` $3,392,434, eligible_unseen_below_floor_count=1, batch_selected=["DENT/USDT"].
- Only eligible unseen below-floor candidate: `DENT/USDT` (rank 1989, mcap $3,269,215, `kucoin_usdt_pair=true`, `exclusion_reason=null`). No fixture (`data/fixtures/DENT_USDT.csv` absent) and no grid coverage in `results/` → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete (18150/18150); mutations NOT_PROMOTED; `FINAL_DECISION.md` records program-level rejection. Git tree clean.

**What to do:**
1. Re-verify gate eligibility: compare current UTC time against `next_eligible_refresh_at` in `universe/last_scan.json`; confirm the file is unchanged.
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_19fbd8c47001bdVTRQ36qHnW8N` due `2026-11-04T01:40:00.000Z` (retain).
