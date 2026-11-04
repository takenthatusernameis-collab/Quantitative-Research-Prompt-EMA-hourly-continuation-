# Initial Task for Next Agent
Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-04T04:37:56Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE until then (~22h04m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid) and independent time comparison at env time `2026-11-04T04:37:56Z`. Gate status re-derived independently via `scripts.refresh_gate.gate_status(state)`: eligible=false, bound=`2026-11-05T02:42:21.634264+00:00`, reason="the 24 h refresh bound has not elapsed yet".
- State `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, snapshot_path `universe/mcap_snapshot_20261104_024221.json`, scanned_at `2026-11-04T02:42:21.634264+00:00`, recorded_at `2026-11-04T02:42:21.885606+00:00`, snapshot_source `CoinGecko public API /api/v3/coins/markets (vs_currency=usd, order=market_cap_desc)`.
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3222980, coverage_reaches_below_floor=true.
- Universe_n=275, expansion floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1, batch_selected=["SUKU/USDT"].
- Candidate: `SUKU/USDT` (rank 1996, mcap $3,231,609). Coverage re-verified: `data/fixtures/SUKU_USDT.csv` absent (ls exit=2), no `SUKU` references in `results/` (grep no matches) → no fixtures/grid coverage, so `--apply` MUST NOT run.
- Baseline grid `results/20261019_135940_grid` complete (18150/18150). `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-05T02:42:21.634264+00:00`).
2. Do NOT run snapshot pass yet (gate closed). If gate logic differs, do not query provider; use `--apply-from` only if applying an existing frozen snapshot with coverage.
3. Review `SUKU/USDT` for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_1a488323b001plz6i4dUtUGZkO` due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Gate closed for ~22h04m from 2026-11-04T04:37:56Z.
