Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-05T19:03:44Z):**
- Gate `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00`. NOT ELIGIBLE until then (~8h38m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid, file unchanged) and independent time comparison at env time `2026-11-05T19:03:44Z`.
- State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261105_034137`, scanned_at=`2026-11-05T03:41:37.153817+00:00`, universe_n=275, expansion_floor=`PIXEL/USDT` $3,351,513, eligible_unseen_below_floor_count=0, batch_selected=[].
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3318550, coverage_reaches_below_floor=true.
- Candidate pool empty below floor; `data/fixtures/SUKU_USDT.csv` absent and no SUKU refs in `results/` → no fixtures/grid coverage, so `--apply` MUST NOT run.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-06T03:41:37.153817+00:00`).
2. If still not eligible: record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_1acfe828b001mLmAYhu4YuOtiO` due `2026-11-06T03:46:56Z` (5 min after gate opens). Retain — do not re-schedule a duplicate.
" filePath">
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md