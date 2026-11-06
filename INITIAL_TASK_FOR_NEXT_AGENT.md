Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` (latest record), `universe/last_scan.json`.

**Current state (verified 2026-11-06T10:16:13Z this session; source of truth `universe/last_scan.json`):**
- `next_eligible_refresh_at` = `2026-11-07T10:16:12.893046+00:00`. **NOT ELIGIBLE** until then (~24h remaining). Independent derivation (Python `json.load` + `datetime.now(timezone.utc)`): eligible=false, bound=`2026-11-07T10:16:12.893046+00:00`, now=`2026-11-06T10:16:13.427723+00:00`, remaining=86399.5s.
- State unchanged: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261106_101612`, `snapshot_path=universe/mcap_snapshot_20261106_101612.json`, `scanned_at=2026-11-06T10:16:12.893046+00:00`, coverage pages_requested=20/pages_fetched=20/all_requested_pages_returned=true/entries_count=2000/lowest_rank_covered=2000/lowest_market_cap_usd=3179353, `coverage_reaches_below_floor=true`, universe_n=275, expansion_floor={PIXEL/USDT, $3,254,887}, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- **The 2026-11-06T10:16 pass found 0 eligible unseen names below the floor.** Independent audit of the fresh snapshot: 22 entries strictly below the floor ($3,254,887) — all excluded (18 `no_tradable_kucoin_spot_usdt_pair`, 4 `insufficient_hourly_history_for_grid`); 0 with `exclusion_reason=None`. Not a coverage shortfall: lowest covered rank 2000 at $3,179,353 < floor $3,254,887, and `history_probe_failure_count=0`. Coverage: `data/fixtures/SUKU_USDT.csv` ABSENT; no `SUKU` refs in `results/` — no fixture/grid coverage. **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete (`all_symbols_processed=true`, `stopped=false`, `stop_reason=null`, `next_cell=null`). `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.
- Wakeup scheduled this session: `wku_1b05cb623001MLKKonA1bXYcvJ` due `2026-11-07T10:21:00Z` (~5 min after gate opens). Do **not** re-schedule a duplicate.

**What to do:**
1. Re-verify gate eligibility at start from `universe/last_scan.json` (do not guess). NOT ELIGIBLE until `2026-11-07T10:16:12.893046+00:00`.
2. If still not eligible: make **no provider calls**. Record an offline check in `NEXT_AGENT_TASK.md` (with exact now/bound/remaining and state evidence), update this handoff if needed, and stop. Rely on the scheduled wakeup; do not schedule duplicates.
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without verified coverage.
4. Never: rerun grids, fetch candles, place orders, change EMA/cost/fill assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory.

**Constraints:** historical research only; free public data/no-cost tooling; preserve negative/blocked results; follow `AGENTS.md` gate policy.