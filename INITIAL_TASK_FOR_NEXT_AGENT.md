Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (verified 2026-11-05T23:20:10Z, source of truth `universe/last_scan.json`):**
- `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00`. **NOT ELIGIBLE** until then (~4.36h remaining). Re-derived independently via Python (`json.load` + `datetime.now(timezone.utc)`): eligible=false, bound=`2026-11-06T03:41:37.153817+00:00`, now=`2026-11-05T23:20:10.811162+00:00`, remaining=15686s (~4:21:26).
- `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261105_034137`, snapshot_path `universe/mcap_snapshot_20261105_034137.json`, scanned_at `2026-11-05T03:41:37.153817+00:00`, recorded_at `2026-11-05T03:50:25.768623+00:00`.
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3318550, coverage_reaches_below_floor=true.
- `universe_n=275`, expansion_floor `{PIXEL/USDT, $3,351,513}`, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- No candidate coverage issue beyond state: `data/fixtures/SUKU_USDT.csv` absent and no `SUKU` refs in `results/` (historical note). `--apply` MUST NOT run without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.

**What to do:**
1. Re-verify gate eligibility at start from `universe/last_scan.json` (do not guess). NOT ELIGIBLE until `2026-11-06T03:41:37.153817+00:00`.
2. If still not eligible: make **no provider calls**. Record an offline check in `NEXT_AGENT_TASK.md` (with exact now/bound/remaining and state evidence), update this handoff if needed, and stop. Rely on the scheduled wakeup; do not schedule duplicates.
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without verified coverage.
4. Never: rerun grids, fetch candles, place orders, change EMA/cost/fill assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory.

**Constraints:** historical research only; free public data/no-cost tooling; preserve negative/blocked results; follow `AGENTS.md` gate policy.

**Wakeup:** scheduled due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.
