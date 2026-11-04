# Initial Task for Next Agent

Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-04T02:42:21Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00` (set by completed snapshot pass). NOT ELIGIBLE until then.
- State `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221.json`, scanned_at `2026-11-04T02:42:21.634264+00:00`, coverage 20/20 pages, 2000 entries, universe_n=275, expansion floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1, batch_selected=["SUKU/USDT"].
- Only eligible unseen below-floor candidate: `SUKU/USDT` (rank 1996, mcap $3,231,609). No fixture (`data/fixtures/SUKU_USDT.csv` absent) and no grid config in `results/` → `--apply` must NOT run without coverage.
- Prior candidate `DENT/USDT` remains without coverage. New snapshot pass completed successfully (gate opened, provider queried once). Git tree clean.

**What to do:**
1. Re-verify gate eligibility (will be NOT ELIGIBLE until 2026-11-05T02:42:21.634264+00:00).
2. Do NOT run snapshot pass yet (gate closed). If somehow gate logic differs, do not query provider; use `--apply-from` only if applying an existing frozen snapshot with coverage.
3. Review `SUKU/USDT` for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** Retain existing wakeup if present or schedule as appropriate. Gate closed for 24h from 2026-11-04T02:42:21.634264+00:00.
