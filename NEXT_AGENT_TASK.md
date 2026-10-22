# NEXT TASK — gated universe refresh and expansion (updated 2026-10-22T17:25Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`. Live cell progress is in `results/20261022_134500_grid/progress.json` (rewritten after every symbol — the source of truth for the running count).

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `MUTATION_RUNNING` |
| Stricter-trend mutation | **running** — `results/20261022_134500_grid`, `stricter_trend: true` (single-variable; everything else — costs 10/2 bps, rr 1.0, conservative exit, risk sizing, folds, entry/exit, §3.4 gates — unchanged; ATR stays closed). |
| Background writer | `bgp_165bcd2e9001EGNNNecrYS0WMP` (pid 4300 + 4 workers), **persistent**, sole writer on this run directory. Restarted this session (no prior writer alive). |
| Progress | 5 280 / 18 150 cells on disk (275 symbols × 66 pairs); next cell `JASMY/USDT P8_12`; `stopped=true`, `stop_reason=in_progress`, `all_symbols_processed=false`. Writer restarted this session: `bgp_165bcd2e9001EGNNNecrYS0WMP` (pid 4300), persistent. The grid runs across sessions — **do not start a second writer**. |
| Baseline grid | `results/20261019_135940_grid` — complete, 0 blocked |
| Universe | N = 275, floor `ALPINE/USDT` $3 614 141 |
| Frozen snapshot | `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z) |
| Next eligible universe refresh | **2026-10-23T12:15:58Z** — no provider contact before then |
| ATR min-risk mutation | closed `NOT_PROMOTED` |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) — environment provisioned (pandas 3.1.0, pytest 9.1.1) |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify state offline and stop cleanly. The expansion belongs to the first session that runs after the bound. The mutation work below is fully offline (uses existing fixtures) and may run at any time.

---

## 2. The task (single-variable mutation of the expanded baseline — offline, safe at any time)

### 2.1 Monitor / complete the stricter-trend mutation grid

The expansion finished at 2026-10-22T13:20Z: N = 275, floor `ALPINE/USDT` $3 614 141, mean net PF 0.4987, 37 cells net PF > 1, candidate_check rejected all, tests 249 passed. The baseline grid `results/20261019_135940_grid` is the 275-symbol expanded baseline (18 150 cells).

One registered variable is flipped on the expanded baseline: `stricter_trend: true` (PROMPT.md §5.1 — entry also requires close above/below EMAslow). The ATR min-risk filter stays closed (`NOT_PROMOTED`). Registered costs, rr 1.0, conservative exit, risk sizing, folds, entry/exit semantics and §3.4 gates are unchanged.

The grid is durable and resumable: cells whose `summary.json` already exist are skipped, and `progress.json` is rewritten after every symbol. Resume command (run from the repository root; skips completed cells — **do not start a second writer** on this run directory):

```bash
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261022_134500_grid --stricter-trend --workers 4 --parent-run results/20261019_135940_grid
```

A persistent writer is now running (`bgp_165bcd2e9001EGNNNecrYS0WMP`, pid 4300). Check `background_process status` / `logs` before re-invoking; only re-invoke if the writer is not running. Record `next_cell` from `progress.json` at each stop. Mutate **one variable at a time** (`stricter_trend` only).

### 2.2 After the mutation grid completes (`next_cell = null`)

```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_eval.py --child results/20261022_134500_grid --parent results/20261019_135940_grid
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261022_134500_grid   # child's own randomized null
PYTHONPATH=. python3 scripts/mutation_repro_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 scripts/mutation_survivor_check.py --run results/20261022_134500_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```

Then record a `NOT_PROMOTED` or promoted decision for child `C_stricter_trend` in `results/mutations.json`, close the entry, update `universe/mcap_expansion_log.md` unchanged (no universe change), and update this handoff.

### 2.3 What must not happen

- No provider call before 2026-10-23T12:15:58Z.
- No re-run of the baseline grid, no second writer on `results/20261022_134500_grid`, no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Mutate one variable at a time: `stricter_trend` only; do not combine with `--min-risk-atr`, `--rr`, or `--aggressive-exit` in this run.

---

## 3. Acceptance checklist

- [ ] Stricter-trend mutation grid completes: 18 150 / 18 150 cells, 0 blocked, `next_cell = null`, `all_symbols_processed = true`.
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
- Use `start` + `logs`/`status` for background processes (not `monitor` to follow running processes).

(End of file)
