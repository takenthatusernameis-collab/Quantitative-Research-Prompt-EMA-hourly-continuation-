# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Handoff updated:** 2026-11-19T08:58:11Z (offline gate check only; NOT ELIGIBLE; no provider calls; no `--apply`; no grid rerun; no wakeups). Read `README.md`, `AGENTS.md`, `PROMPT.md` (§2.1.2, §2.1.5), `NEXT_AGENT_TASK.md`, `universe/last_scan.json` and `universe/mcap_rank.json` first.

## 1. Status at handoff

- **Gate:** bound `2026-11-19T19:50:23.792771+00:00` (`universe/last_scan.json` `next_eligible_refresh_at`). Recomputed offline at `2026-11-19T08:58:11Z` via `scripts/refresh_gate.py:gate_status` and `scripts/refresh_universe.py plan` → **NOT ELIGIBLE** (remaining 10h52m12.8s / 39,132.8s). **No provider calls made this session.**
- Scan state: **`AWAITING_NEW_ELIGIBLE_CANDIDATES`**, snapshot_id=`mcap_snapshot_20261118_195023`, scanned_at=`2026-11-18T19:50:23.792771+00:00`, CoinGecko `/api/v3/coins/markets` (usd, market_cap_desc), 25/25 pages, 2500 entries, `coverage_reaches_below_floor=true`, lowest mcap **$1,484,631**, universe_n=278, expansion floor **CERE/USDT $1,528,741**.
- Batch selected: **`[]`** — `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`.
- **Blockers (unchanged, verified this session):** no new candidates below the floor. Baseline grid remains 278 symbols / 18,348/18,348 cells complete, unchanged.
- `universe/mcap_rank.json` unchanged (n_symbols=278). Preserved artifacts intact: `results/FINAL_DECISION.md`, grid progress/snapshot files. No fixtures/candles fetched, no `--apply`, no grid expansion/reruns, no EMA signal/fill/cost changes, no orders. `cron_list` empty.
- **Environment:** `python3` 3.12.3 with `pandas` 3.1.1, `numpy` 2.5.5, `pytest` 9.2.0, `requests` 2.31.0 (installed via `pip install --user` under temp home `/home/runner/work/_temp/kilo-home/.local` — **re-verify at start of next session**; if missing, reinstall before any grid/signal/pytest work). Gate tooling remains stdlib-only.

## 2. Your task (measurable, one item)

1. **Offline first.** Recompute eligibility from `next_eligible_refresh_at` (`2026-11-19T19:50:23.792771+00:00`) against independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess. Expected **NOT ELIGIBLE** until bound.
2. **If NOT eligible:** make **no provider calls**. Append exactly one concise offline gate-check line (exact now/bound/remaining, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `eligible_unseen_below_floor_count=0`, batch none pending, blockers unchanged) to `NEXT_AGENT_TASK.md` log and section 3 below; stop. Do not schedule wakeups (`cron_list` must stay empty). Expected NOT ELIGIBLE until 2026-11-19T19:50:23.792771Z.
3. **If eligible:** only take a new provider pass if required by policy/state; prefer resolving recorded batch first when environment allows. Before any `--apply` verify fixture + baseline grid coverage in `results/20261019_135940_grid/progress.json` for every selected candidate; if any lacks either, **do not apply** and record blocker per candidate.
4. **Batch resolution (when env permits):** for any new candidates confirm tradable KuCoin spot USDT identity/price and sufficient hourly history, fetch fixtures only for new symbols, validate integrity, expand grid only for new symbols via resume path (no rerun of existing cells, no re-fetch of grid-used fixtures), then apply only after all candidates covered. Never change EMA signal/fill/cost assumptions or use fixtures as market evidence.

## 3. Gate-check log (append one line per offline check)

| UTC now | Bound | Remaining | Outcome |
| --- | --- | --- | --- |
| 2026-11-19T08:58:11Z | 2026-11-19T19:50:23.792771Z | 10h52m12.8s (39,132.8s) | NOT ELIGIBLE; offline gate recomputed via `scripts/refresh_gate.py:gate_status` (eligible=false, bound not elapsed), `scripts/refresh_universe.py plan` → `refresh_allowed_now=false`, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261118_195023`, floor CERE/USDT $1,528,741, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, batch none pending, no provider calls. Universe verified: `universe_n=278`, `symbols_without_fixture=[]`, `symbols_without_grid_cells=[]`; grid `completed_cells=18348`, `n_symbols=278` (18348 == 278×66). Env: pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3. No apply, no fixtures, no candles, no grid rerun, no orders, no wakeups. |