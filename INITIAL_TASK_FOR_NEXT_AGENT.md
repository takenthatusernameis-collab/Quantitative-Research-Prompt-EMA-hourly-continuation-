Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-19T09:12:17Z):**
- Gate `next_eligible_refresh_at` = `2026-11-19T19:50:23.792771+00:00`. NOT ELIGIBLE until then (~10h38m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid, file unchanged) and independent time comparison at env time `2026-11-19T09:12:17Z`. Gate status re-derived via `scripts.refresh_gate.gate_status(state)` (PYTHONPATH=.): eligible=false, bound=`2026-11-19T19:50:23.792771+00:00`, reason="the 24 h refresh bound has not elapsed yet". State unchanged: snapshot_id=`mcap_snapshot_20261118_195023`, scanned_at=`2026-11-18T19:50:23.792771+00:00`, universe_n=278, expansion_floor=`CERE/USDT` $1,528,741, eligible_unseen_below_floor_count=0, batch_selected=[].
- State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261118_195023`, snapshot_path `universe/mcap_snapshot_20261118_195023.json`, scanned_at `2026-11-18T19:50:23.792771+00:00`, recorded_at `2026-11-18T19:50:24.206114+00:00`, snapshot_source `CoinGecko public API /api/v3/coins/markets (vs_currency=usd, order=market_cap_desc)`.
- Coverage: pages_requested=25, pages_fetched=25, all_requested_pages_returned=true, entries_count=2500, lowest_rank_covered=2500, lowest_market_cap_usd=1484631, coverage_reaches_below_floor=true.
- Universe_n=278, expansion floor `CERE/USDT` $1,528,741, eligible_unseen_below_floor_count=0, batch_selected=[] (no new candidates).
- Baseline grid `results/20261019_135940_grid` complete (18348/18348 cells, 278 symbols × 66 pairs, all_symbols_processed=true, stopped=false, next_cell=null). `results/FINAL_DECISION.md` records program-level rejection. Git tree clean (`git status --short` empty, `git diff --stat` empty).
- Env verified: pandas 3.1.1, numpy 2.5.5, pytest 9.2.0, requests 2.31.0, python 3.12.3.

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-19T19:50:23.792771+00:00`).
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 25-page snapshot pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** None scheduled. Next gate eligibility at `2026-11-19T19:50:23.792771+00:00`. Do not schedule a wakeup — the next agent will run on its own schedule.