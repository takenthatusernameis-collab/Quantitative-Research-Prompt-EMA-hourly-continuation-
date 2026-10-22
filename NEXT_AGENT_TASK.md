# NEXT TASK — gated universe refresh and expansion (updated 2026-10-22T14:36Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `MUTATION_RUNNING` (stricter-trend child `results/20261022_134500_grid`, background process `bgp_163dac260001iUtpf1UG3qqleM` pid 19110) |
| Baseline grid (program grid) | `results/20261019_135940_grid` — 275 symbols × 66 pairs = 18 150 cells, complete, 0 blocked |
| Universe | N = 275, floor `ALPINE/USDT` $3 614 141 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z, 20/20 pages, 2 000 entries, lowest covered $3 490 223) |
| Last offline verification (this session) | `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. No provider contact this session. |
| **Next eligible universe refresh** | **2026-10-23T12:15:58Z** (24 h after the 12:15:58Z snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see `results/mutations.json`) |
| Stricter-trend mutation | **running** — `results/20261022_134500_grid`, `stricter_trend: true` (single-variable, everything else registered), 4356/18 150 cells complete, next cell `BTT/USDT P8_12`. `stopped=true`, `stop_reason=in_progress`, `all_symbols_processed=false`. Background process `bgp_163dac260001iUtpf1UG3qqleM` (pid 19110) still running, persistent. |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) |
| Tooling | `scripts/run_mutation_grid.py` (resumable parallel mutation runner), `scripts/aggregate_grid.py`, `scripts/candidate_check.py`, `scripts/mutation_eval.py`, `scripts/null_grid_scan.py`; `scripts/refresh_gate.py` enforces the 24 h bound |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify the state offline and stop cleanly. The expansion belongs to the first session that runs after the bound. The mutation work below is fully offline (uses existing fixtures) and may run at any time.

---

## 2. The task (single-variable mutation of the expanded baseline — offline, safe at any time)

The expansion finished at 2026-10-22T13:20Z: ALPINE/USDT grid 66/66 cells, N = 275, floor `ALPINE/USDT` $3 614 141, mean net PF 0.4987, 37 cells net PF > 1, candidate_check rejected all, tests 249 passed. The baseline grid `results/20261019_135940_grid` is now the 275-symbol expanded baseline (18 150 cells).

### 2.1 Resume / run the stricter-trend mutation grid

One registered variable is flipped on the expanded baseline: `stricter_trend: true` (PROMPT.md §5.1 — entry also requires close above/below EMAslow). The ATR min-risk filter stays closed (`NOT_PROMOTED`). Registered costs (10 bps taker + 2 bps slippage per side), rr 1.0, conservative exit, risk sizing, folds, entry/exit semantics and §3.4 gates are unchanged.

The grid is durable and resumable: cells whose `summary.json` already exist are skipped, and `progress.json` is rewritten after every symbol. A persistent background process is running:

```bash
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261022_134500_grid --stricter-trend --workers 4 --parent-run results/20261019_135940_grid
```

Progress as of 2026-10-22T17:09Z: **4 752 / 18 150 cells** complete, next cell `CFX/USDT P8_12`, `stopped=true`, `stop_reason=in_progress`, `all_symbols_processed=false`. The grid process is NOT running in this session (no background processes available); the host environment here lacks `pandas`/`pytest`, so the grid could not be resumed from this session. Re-running the resume command (below) from a properly provisioned environment resumes from `progress.json` — do not start a second writer on this run directory.
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

Then record a `NOT_PROMOTED` or promoted decision in `results/mutations.json` (child `C_stricter_trend`), close the entry, update `universe/mcap_expansion_log.md` unchanged (no universe change), and update this handoff.

### 2.3 What must not happen

- No provider call before 2026-10-23T12:15:58Z.
- No re-run of the baseline grid, no second writer on `results/20261022_134500_grid`, no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Mutate one variable at a time: `stricter_trend` only; do not combine with `--min-risk-atr`, `--rr`, or `--aggressive-exit` in this run.

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
