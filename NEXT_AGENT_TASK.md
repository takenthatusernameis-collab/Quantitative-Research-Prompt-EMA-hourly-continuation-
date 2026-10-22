# NEXT TASK — gated universe refresh and expansion (updated 2026-10-22T10:22Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `MUTATION_RUNNING` (stricter-trend child `results/20261022_134500_grid`, 264/18 150 cells, next cell `XRP/USDT P8_12`; persistent background process) |
| Baseline grid (program grid) | `results/20261019_135940_grid` — 275 symbols × 66 pairs = 18 150 cells, complete, 0 blocked |
| Universe | N = 275, floor `ALPINE/USDT` $3 614 141 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z, 20/20 pages, 2 000 entries, lowest covered $3 490 223) |
| Last offline verification (this session) | 2026-10-22T13:54Z — expansion complete (ALPINE/USDT 66/66 cells); `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Stricter-trend mutation grid launched (see below). No provider contact this session. |
| **Next eligible universe refresh** | **2026-10-23T12:15:58Z** (24 h after the 12:15:58Z snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see `results/mutations.json`) |
| Stricter-trend mutation | **running** — `results/20261022_134500_grid`, `stricter_trend: true` (single-variable, everything else registered), 264/18 150 cells complete, next cell `XRP/USDT P8_12`, resume command below |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) |
| Tooling | `scripts/run_mutation_grid.py` (resumable parallel mutation runner), `scripts/aggregate_grid.py`, `scripts/candidate_check.py`, `scripts/mutation_eval.py`, `scripts/null_grid_scan.py`; `scripts/refresh_gate.py` enforces the 24 h bound |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify the state offline and stop cleanly. The expansion belongs to the first session that runs after the bound. The mutation work below is fully offline (uses existing fixtures) and may run at any time.

**Session 2026-10-22T10:28Z (this session).** Offline only — bound not yet elapsed (10:28 < 11:41:20). `refresh_universe.py plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session (no CoinGecko, no KuCoin). `universe/last_scan.json` verification note rewritten with this session's timestamp. Session stopped cleanly; nothing was fetched. The single gated ranking pass + expansion belongs to the first session after 2026-10-22T11:41:20Z.
**Session 2026-10-22T09:52Z (this session).** Offline only — bound not yet elapsed (09:52 < 11:41:20). `plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session. The verification note in `universe/last_scan.json` was rewritten with this session's timestamp. A wakeup is scheduled for **2026-10-22T11:42:00Z** to run the single gated ranking pass + expansion once the bound opens.
**Session 2026-10-22T09:45Z.** Offline only — bound not yet elapsed (09:45 < 11:41:20). `plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session. Session stopped cleanly; nothing was fetched.
**Session 2026-10-22T09:40Z.** Offline only — bound not yet elapsed (09:40 < 11:41:20). `plan` → `refresh_allowed_now: false`; `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps. Tests 249 passed. Outbound HTTPS confirmed (non-provider host). A wakeup is scheduled for **2026-10-22T11:42:00Z** to run the single gated ranking pass + expansion once the bound opens; no provider contact this session.
**Session 2026-10-22T08:49Z.** Offline only — bound not yet elapsed (08:49 < 11:41:20). `plan` → `refresh_allowed_now: false`; `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Tests 249 passed. A wakeup was scheduled for 2026-10-22T11:42:00Z to run the gated expansion once the bound opens; no provider contact this session.
**Session 2026-10-22T10:52Z (this session).** Offline only — bound not yet elapsed (10:52 < 11:41:20). `refresh_universe.py plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. No provider contact this session (no CoinGecko, no KuCoin). `universe/last_scan.json` verification note rewritten with this session's timestamp. Session stopped cleanly; nothing was fetched. The single gated ranking pass + expansion belongs to the first session after 2026-10-22T11:41:20Z.
**Fixture count note.** 268 fixture files on disk vs. N=266: the two extras are `CCD/USDT` and `sample_hourly`. `sample_hourly` is the synthetic template used by `scripts/run_baseline.py` / `scripts/cost_stress.py` (no manifest row). `CCD/USDT` (Concordium) is **eligible but above the expansion floor** — snapshot rank 552, $41 673 734, tradable KuCoin pair, its fixture is pre-fetched and valid (22 099 rows) — and it was deliberately kept out of the universe by the strict append-only rule of PROMPT.md §2.1.2 (documented in `universe/mcap_expansion_log.md`, "Names deliberately skipped", together with `GAS`, rank 322, $82 731 692). Both have no grid cells and enter the universe only if a later snapshot puts them below the floor. Neither is in `universe/mcap_rank.json`, so neither is ever re-fetched or re-gridded. `data/fixtures/fetch_manifest.json` has 267 rows (266 universe symbols + CCD; the template has none).

**Working directory.** Run commands from the repository root.

---

## 2. The task (single-variable mutation of the expanded baseline — offline, safe at any time)

The expansion finished at 2026-10-22T13:20Z: ALPINE/USDT grid 66/66 cells, N = 275, floor `ALPINE/USDT` $3 614 141, mean net PF 0.4987, 37 cells net PF > 1, candidate_check rejected all, tests 249 passed. The baseline grid `results/20261019_135940_grid` is now the 275-symbol expanded baseline (18 150 cells).

### 2.1 Resume / run the stricter-trend mutation grid

One registered variable is flipped on the expanded baseline: `stricter_trend: true` (PROMPT.md §5.1 — entry also requires close above/below EMAslow). The ATR min-risk filter stays closed (`NOT_PROMOTED`). Registered costs (10 bps taker + 2 bps slippage per side), rr 1.0, conservative exit, risk sizing, folds, entry/exit semantics and §3.4 gates are unchanged.

The grid is durable and resumable: cells whose `summary.json` already exist are skipped, and `progress.json` is rewritten after every symbol. A persistent background process is running:
```bash
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261022_134500_grid --stricter-trend --workers 4 --parent-run results/20261019_135940_grid
```
Progress as of 2026-10-22T13:54Z: 264 / 18 150 cells (4 symbols complete), next cell `XRP/USDT P8_12`. Re-running the same command resumes from `progress.json` — do not start a second writer on this run directory. Full grid needs ~2+ hours, so it spans sessions; record `next_cell` in this handoff at each stop.

### 2.2 After the mutation grid completes

```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_eval.py --child results/20261022_134500_grid --parent results/20261019_135940_grid
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261022_134500_grid   # child's own randomized null
PYTHONPATH=. python3 scripts/mutation_repro_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_survivor_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```
Then record a `NOT_PROMOTED` or promoted decision in `results/mutations.json` (child `C_stricter_trend`), close the entry, update `universe/mcap_expansion_log.md` is unchanged (no universe change), and update this handoff.

### 2.3 What must not happen
- No provider call before 2026-10-23T12:15:58Z.
- No re-run of the baseline grid, no second writer on `results/20261022_134500_grid`, no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Mutate one variable at a time: `stricter_trend` only; do not combine with `--min-risk-atr`, `--rr`, or `--aggressive-exit` in this run.

---

**Session 2026-10-22T13:54Z (this session).** Expansion verified complete (N=275, ALPINE/USDT 66/66 cells, 18 150/18 150, 0 blocked; aggregate mean net PF 0.4987; candidate_check rejected all; tests 249 passed). Stricter-trend mutation grid `results/20261022_134500_grid` launched as a persistent background process (4 workers): 264/18 150 cells complete, next cell `XRP/USDT P8_12`. `results/mutations.json` updated with child `C_stricter_trend` (status `running`). No provider contact (next refresh bound 2026-10-23T12:15:58Z). Next agent: resume the mutation grid to completion, then run the evaluation legs (§2.2) and record the decision.

---

## 3. Acceptance checklist
- [ ] Stricter-trend mutation grid completes: 18 150 / 18 150 cells (275 symbols × 66 pairs), 0 blocked, `next_cell = null`, `all_symbols_processed = true`.
- [ ] `results/mutations.json` child `C_stricter_trend` has `status = complete` with progress and a recorded `NOT_PROMOTED`/promoted `decision`.
- [ ] `aggregate_grid.py --run results/20261022_134500_grid` produces the child pooled report; parent baseline numbers stay in `results/mutations.json` → `parent.pooled`.
- [ ] `candidate_check.py` against the stricter-trend grid: verdict per cell, 0 promoted without full §3.4 gates.
- [ ] `mutation_eval.py` parent vs child (full 18 150 cells): pooled net PF delta, OOS net PF, 2x-cost stress, cells clearing gate, walk-forward.
- [ ] `null_grid_scan.py` on the child grid: child's own randomized null (Bonferroni over 18 150 cells); selection vs null reported.
- [ ] `mutation_repro_check.py` and `mutation_survivor_check.py` on gate-clearing cells; reproduction matches stored artifacts.
- [ ] `PYTHONPATH=. python3 -m pytest tests/ -q` passes (249 passed baseline; no new failures).
- [ ] No provider contact before 2026-10-23T12:15:58Z; no second writer on the mutation run dir; no change to registered costs/folds/gates.

---

## 4. What must not happen
- No provider call before 2026-10-23T12:15:58Z, no second ranking pass inside the 24 h window.
- No re-run of baseline grid, no second worker on any run directory, no promotion from a child grid.
- No change to registered grid, cost model, fill rule, folds, or §3.4 gates.
- Use `start` + `logs`/`status` for background processes (not `monitor` action to follow running processes).

---

**Session 2026-10-22T13:20Z.** Grid completed for ALPINE/USDT (66 cells); 18150/18150, 0 blocked. Aggregate: 18150 cells, mean net PF 0.4987, 37 net PF>1, candidate_check rejected all. Tests 249 passed. N=275, floor ALPINE/USDT $3 614 141. Next refresh 2026-10-23T12:15:58Z. Next agent: single-variable mutation of expanded baseline.
