# Initial Task for Next Agent

Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-04T03:51:02Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE until then (~22h51m remaining). Verified at `2026-11-04T03:51:02Z` via direct read of `universe/last_scan.json`.
- State `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, scanned_at `2026-11-04T02:42:21.634264+00:00`, coverage 20/20 pages, 2000 entries, universe_n=275, expansion floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1, batch_selected=["SUKU/USDT"].
- Independent snapshot reconciliation of `universe/mcap_snapshot_20261104_024221.json`: `fetched_at`==`last_scan.scanned_at` (2026-11-04T02:42:21.634264+00:00), pages_fetched==pages_requested==20, `all_requested_pages_returned`=true, entries_count==len(entries)==2000, lowest_rank_covered==2000, lowest_market_cap_usd==3222980. Below-floor band (mcap < $3,404,245): 40 entries; 39 excluded; exactly 1 eligible unseen: `SUKU/USDT` (rank 1996, mcap $3,231,609, `kucoin_usdt_pair=true`, `exclusion_reason=null`).
- Only eligible unseen below-floor candidate: `SUKU/USDT`. No fixture (`data/fixtures/SUKU_USDT.csv` absent) and no grid config in `results/` (grep no matches) → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete (18150/18150 cells, 275 symbols × 66 pairs, pooled net PF 0.4987). `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.

**What to do:**
1. Re-verify gate eligibility (NOT ELIGIBLE until 2026-11-05T02:42:21.634264+00:00).
2. Do NOT run snapshot pass yet (gate closed). If gate logic differs, do not query provider; use `--apply-from` only if applying an existing frozen snapshot with coverage.
3. Review `SUKU/USDT` for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_1a488323b001plz6i4dUtUGZkO` due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Gate closed for ~22h51m from 2026-11-04T03:51:02Z.
"""