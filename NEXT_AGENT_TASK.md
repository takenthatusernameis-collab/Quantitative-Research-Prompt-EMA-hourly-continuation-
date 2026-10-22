# AUTHORIZED MAINTENANCE UPDATE — 2026-10-22 (session 3 of the run that opened 2026-10-21T22:29Z)

**Read this file first.** It supersedes the handoffs of 2026-10-21T19:50Z and
2026-10-21T22:32Z. The durable record of the mutation is `results/mutations.json`
(`children.C_min_risk_atr`).

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Baseline grid (the program's grid) | `results/20261019_135940_grid` — 266 symbols × 66 pairs = 17 556 cells, complete |
| Universe | N = 266, floor AGLD/USDT $16 279 472 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261021_114120.json` (fetched 2026-10-21T11:41:20Z) |
| **Next eligible universe refresh** | **2026-10-22T11:41:20Z** (24 h after the snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see §5) |
| Tests | `198 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T02:39Z) |

**Provider discipline (unchanged).** Until 2026-10-22T11:41:20Z the market-data
provider must not be contacted at all — no polling, no "quick check", no
partial refresh. After that timestamp exactly one fetch is allowed; the new
snapshot is then frozen for the following 24 h. Repeated provider polling is
not a way to make progress here and it is not a task.

---

## 2. Run ownership was reconciled before anything was started

The previous handoff said "4 workers alive, do not start a second runner".
That statement was stale: the worker process had lived in the *previous*
Actions runner container, which was gone.

Evidence collected before any compute was started (2026-10-22T22:35Z–22:40Z):

* `ps -eo pid,ppid,etime,cmd` showed **no** `run_mutation_grid.py` process; the
  container had been started at 22:29Z by the current workflow run.
* `.github/workflows/main.yml` declares `concurrency: group: kilo-repository,
  cancel-in-progress: false`, so no second workflow activation can write to
  the repository while this one is running.
* `results/20261021_172619_grid/progress.json` was frozen at 11 484/17 556
  cells, and a disk audit of the cell artifacts found **11 598** cells with a
  `summary.json` (the progress counter lagged the artifacts by one partial
  symbol group).

Therefore the only writer was gone and the run was resumable through the
repository's own tested resume path. Before resuming, the environment was
proved to be the one that produced the stored artifacts:

```
PYTHONPATH=. python3 scripts/mutation_repro_check.py --sample 3 --out /tmp/env_repro_check
→ child reproduced True / parent reproduced True for 3/3 sampled cells
```

(`numpy 2.5.4`, `pandas 3.0.6` — the installed versions reproduce the stored
blotters and summaries bit for bit.)

---

## 3. The child grid was resumed and completed

Command (the repository's own resume path; it skips every cell that already
has a `summary.json`):

```
PYTHONPATH=. python3 scripts/run_mutation_grid.py \
  --run results/20261021_172619_grid --min-risk-atr --workers 4 \
  --taker-fee-bps 10 --slippage-bps 2 --rr 1.0 --atr-threshold 1.0 \
  --sizing risk --risk-fraction 0.01 --max-notional-multiple 10 \
  --parent-run results/20261019_135940_grid \
  --note "PROMPT.md 5.2 ATR minimum-risk mutation (skip trades whose risk distance < ATR(14) x 1.0); resumed single-variable child of results/20261019_135940_grid after the previous worker container was terminated"
```

Exit code 0. Started 2026-10-22T22:40:52Z, finished 2026-10-22T00:23:56Z.

* `results/20261021_172619_grid/progress.json`: `completed_cells 17556`,
  `next_cell null`, `all_symbols_processed true`, `stopped false`,
  `stop_reason null`, 266 symbols × 66 pairs.
* 0 blocked cells, 0 cell directories without a `summary.json`.
* Integrity scan of every cell directory: **0 problems** (missing, empty or
  unparseable artifacts).
* `results/20261021_172619_grid/run_config.pre_resume_20261021_2243.json` keeps
  the pre-resume `run_config.json` for provenance; the run config itself is
  unchanged except for its timestamp.
* Single-variable check: the child config differs from the parent config in
  exactly one field — `min_risk_atr: false → true` (everything else identical:
  10 bps taker + 2 bps slippage, rr 1.0, ATR threshold 1.0, conservative exit,
  risk sizing 1 % with a 10× notional cap).

**Incident, recorded honestly.** While monitoring the run, the
`background_process monitor` action was used to follow it. That action
*starts* the command it is given, so a second copy of the runner was started
by mistake at 2026-10-22T22:50Z and was stopped 1–2 minutes later
(`bgp_160a8a939001VMh5N5J0hRnqUq`, "Signal received; finishing the running
symbols and writing progress.json"). The original runner (pid 4220) was the
one kept. Both write identical content, but a cell can be written by two
processes at the same time, so the whole grid was audited afterwards: every
cell has a complete artifact set, every `summary.json` parses, and the
full-universe evaluation reports **0 profit-factor mismatches** between the
stored summaries and the stored blotters for both the parent and the child
(`count_pf_mismatches`). The `--verify-sample` leg re-ran 5 further child cells
through the engine with a max absolute metric delta of 0.0. No corruption was
found.

---

## 4. Three defects were fixed before the decision legs were trusted

All three evaluation legs re-ran cells through the real backtest with a
**hard-coded baseline config** (`CONFIG_DEFAULTS`, i.e. `min_risk_atr=false`).
For the ATR child that is the wrong strategy: the screen leg reads the child's
stored blotters, while the "exact" leg re-ran the parent's rule, so the two
legs described two different strategies.

| File | Before | After |
|---|---|---|
| `scripts/run_grid.py` | — | new helper `load_run_config(run_dir)`: the run's own `run_config.json` wins, the engine default is the fallback |
| `scripts/null_grid_scan.py` | `config = dict(CONFIG_DEFAULTS)` | `config = run_config(run_dir)` (the randomized null must randomize the rule that is actually being tested) |
| `scripts/oos_grid_scan.py` | `config = dict(CONFIG_DEFAULTS)` | `config = load_run_config(run_dir)` |
| `scripts/survivor_selection_audit.py` | `config = dict(CONFIG_DEFAULTS)` | `config = load_run_config(run_dir)` |

The baseline is unaffected: the baseline run's config *is* the engine default
(`min_risk_atr=false`), which a test asserts. New regression tests (5 of them,
`198 passed` in total):

* `tests/test_null_grid_scan.py::test_the_null_randomizes_the_rule_of_the_run_it_is_asked_about`
* `tests/test_null_grid_scan.py::test_the_baseline_run_is_unaffected_by_the_config_lookup`
* `tests/test_null_grid_scan.py::test_the_atr_rule_changes_the_real_leg_of_the_null`
* `tests/test_oos_grid_scan.py::test_the_audit_re_runs_the_cells_with_the_runs_own_config`
* `tests/test_survivor_selection_audit.py::test_the_selection_audit_re_runs_the_family_with_the_runs_own_config`

The fix is visible in the artifacts: after it, the screen and the exact
re-run of a child cell agree (e.g. DEXE/USDT P55_200: screen OOS PF 1.8907 →
exact OOS PF 1.9333), while before it the same cell read screen 1.8907 →
exact 1.0253 because the exact leg ran the parent's rule.

---

## 5. The decision legs on the complete child grid (17 556 cells)

All legs ran on the complete grid, both runs, all 266 symbols, 66 pairs.

| Leg | Artifact | Headline |
|---|---|---|
| Parent → child → delta, full universe | `results/20261022_002531_mutation_eval_full` | pooled net PF 0.5225 → **0.7347**; pooled OOS net PF 0.5298 → **0.6676** (2× costs 0.3266 → 0.4781); trades 14 241 237 → 6 913 033; cells clearing the OOS gate 10 → **106**; walk-forward pooled out-of-fold net PF 0.6409 → **0.7390** (2× costs 0.4521 → 0.5731); 0 PF mismatches on both sides |
| Reproduction check, 24 cells | `results/20261022_002531_mutation_repro_check` | 24/24 child and 24/24 parent cells reproduce the stored summary, blotter and equity curve exactly |
| Survivor check, full universe | `results/20261022_002531_mutation_survivor_check` | 106 gate-clearing cells on 39 symbols; family pooled OOS net PF 1.3110 over 8 854 OOS trades; leave-one-symbol-out stable (88/106 cells left, re-selection keeps 10–10); **only 18 of 106** keep PF > 1 in every OOS sub-period |
| Out-of-sample audit | `results/20261022_013800_child_oos_grid_scan` | 17 556 cells; 608 with OOS PF > 1, 591 with ≥ 30 OOS trades; pooled OOS net PF 0.6676; 0 full-sample PF mismatches; 9 *credible candidates* and 111 exploratory signals inside the 120 exactly verified cells (see the cap in §6) |
| Walk-forward re-selection | `results/20261022_021500_child_survivor_selection_audit` | 106-cell family on 39 symbols, family net PF 1.3110 (1.1123 at 2× costs); median in-fold PF 1.0906 → median out-of-fold PF 0.7347; pooled out-of-fold net PF **0.7390** over 60 853 trades; 16.5 % of the out-of-fold windows land above PF 1 against 10.6 % from the grid's own null; the selection ranks at the **55.7th percentile** of that null (p = 2.24e-11) |
| Randomized null, Bonferroni over 17 556 cells | `results/20261021_230500_child_null_grid_scan` | real 613 cells OOS PF > 1 / **103** clearing the gate; **timing null 1 611 / 329**; block null 4 286 / 1 195; sign null 773 / 68; family-wise p for the best cell **0.9933**; the real rule beats its own timing null in 4 521 of 17 556 cells and loses in 13 035; the 106 survivor cells were re-randomized 20× each and **0** of them keep an OOS net PF above the real one at a Bonferroni-corrected level over 17 556 tests; validation 200/200 summary matches, 200/200 signal matches |

### Decision: `NOT_PROMOTED` — the baseline grid stays the program's grid

The four questions are kept apart:

* **Strategy correctness** — fine. The child is a clean single-variable
  mutation of the baseline, every cell reproduces from the fixture on disk,
  the equity reconciles and the profit factors match the blotters.
* **Execution validity** — fine, and improved. The ATR filter halves the
  trade count (14.24 M → 6.91 M) and the cost per trade stays small
  ($8.61 → $10.14 against a gross profit of $1.75 per trade).
* **Statistical evidence** — **fails.** The child's own randomized null
  produces **329** gate-clearing cells against **103** real ones on the same
  17 556 cells; the observed tail is smaller than the null's tail
  (family-wise p 0.9933), and the walk-forward selection ranks at the 55.7th
  percentile of the child's own null. All 106 gate-clearing cells were
  re-randomized 20 times each: **not one** of them keeps an out-of-sample net
  PF above its own randomization at a Bonferroni-corrected level over
  17 556 tests. 88 of the 106 work in one stretch of time only.
* **Economic profitability** — **fails.** The pooled out-of-sample net PF of
  the child grid is 0.6676, and 0.4781 under 2× costs. The procedure never
  reaches a net-profitable out-of-fold window, it only loses less than the
  baseline does.

The child grid stays as a **documented, reproducible negative result** and as
the reference point for the next mutation. It is not a candidate and the
baseline is not replaced.

---

## 6. Deviations and caveats that a reader must know

1. **The out-of-sample audit's exact stage was capped at 120 cells**
   (`--max-verify 120`), so the 9 "credible candidates" and 111 "exploratory
   signals" describe that sample, not all 591 cells with ≥ 30 OOS trades. The
   cap was needed because the window-sensitivity leg of that script re-runs
   the closest survivors at three window lengths (≈ 30 min for the child).
   The family's exact numbers do **not** depend on the cap: the selection
   audit re-runs the whole 106-cell family itself.
2. **The ATR rule breaks the window-equivalence shortcut.** The null harness
   re-runs a cell on the trailing window and compares it with the
   full-history run whose entries are gated at the window start. That
   equivalence holds exactly for the baseline rule (12/12 in the parent's
   validation) but only for **139 of 200** child cells, because ATR(14) at the
   start of a window is not the ATR(14) of the full history. Both sides of
   the null comparison use the same formulation, so the comparison is
   internally consistent, but the child's absolute out-of-sample numbers in
   the null leg (613 / 103) differ slightly from the ones read off the stored
   blotters (608 / 106).
3. **The null leg ran in three passes** over one output directory
   (`results/20261021_230500_child_null_grid_scan`): the grid-wide leg was
   started while the child grid was still being filled (13 716 cells), then
   resumed to the full 17 556 cells, then resumed once more for the survivor
   leg. The final artifact covers all 17 556 cells.
4. **The survivor leg uses 20 replicates per cell**, not the parent's 60,
   because the child's family is 106 cells instead of 10. Fewer replicates
   widen the error bars of the null distribution; they do not bias it.

---

## 7. Exact commands of this session (all exit code 0)

```
# child grid, resumed and completed
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261021_172619_grid \
  --min-risk-atr --workers 4 --taker-fee-bps 10 --slippage-bps 2 --rr 1.0 \
  --atr-threshold 1.0 --sizing risk --risk-fraction 0.01 --max-notional-multiple 10 \
  --parent-run results/20261019_135940_grid --note "PROMPT.md 5.2 ATR minimum-risk mutation ..."

PYTHONPATH=. python3 scripts/mutation_eval.py \
  --parent results/20261019_135940_grid --child results/20261021_172619_grid \
  --yardstick results/20261021_121629_survivor_selection_audit/summary.json \
  --verify-sample 5 --out results/20261022_002531_mutation_eval_full

PYTHONPATH=. python3 scripts/mutation_repro_check.py \
  --parent results/20261019_135940_grid --child results/20261021_172619_grid \
  --sample 24 --out results/20261022_002531_mutation_repro_check

PYTHONPATH=. python3 scripts/mutation_survivor_check.py \
  --child results/20261021_172619_grid --out results/20261022_002531_mutation_survivor_check

PYTHONPATH=. python3 scripts/oos_grid_scan.py \
  --run results/20261021_172619_grid --max-verify 120 \
  --out results/20261022_013800_child_oos_grid_scan

PYTHONPATH=. python3 scripts/survivor_selection_audit.py \
  --run results/20261021_172619_grid \
  --oos-audit results/20261022_013800_child_oos_grid_scan \
  --out results/20261022_021500_child_survivor_selection_audit

# randomized null, three passes over one output directory
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261021_172619_grid \
  --modes timing block sign --survivor-replicates 60 --workers 3 \
  --out results/20261021_230500_child_null_grid_scan
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261021_172619_grid \
  --modes timing block sign --survivor-replicates 20 --workers 3 \
  --out results/20261021_230500_child_null_grid_scan
PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261021_172619_grid \
  --modes timing block sign --survivors-from results/20261022_021500_child_survivor_source \
  --survivor-modes timing block sign --survivor-replicates 20 --control-sample 12 \
  --validate-sample 24 --workers 3 --out results/20261021_230500_child_null_grid_scan

# survivor source of the null leg: the filter over the child's OOS audit that
# results/20261022_021500_child_survivor_source/README.md documents
#   for row in json.load(open('results/20261022_013800_child_oos_grid_scan/cells.jsonl')):
#       if (row['oos_trades'] or 0) >= 30 \
#               and (row['oos_net_pf'] or 0.0) > 1.0 \
#               and (row['oos_stress_net_pf'] or 0.0) > 1.0:
#           keep(row)
# → 106 cells in results/20261022_021500_child_survivor_source/cells.jsonl

PYTHONPATH=. python3 -m pytest tests/ -q     # 198 passed
```

---

## 8. What is still open, and the next task

**Open, in this order:**

1. **The universe refresh becomes eligible at 2026-10-22T11:41:20Z.** Until
   then: do not contact the provider, do not poll, do not "check whether the
   list changed". After that timestamp, one fetch of the new top-of-book
   universe, freeze the new snapshot, and apply the §3.1–§3.3 expansion
   procedure to the new symbols only.
2. **The child grid needs no further work.** Every decision leg is closed and
   recorded in `results/mutations.json`. Do not re-run the mutation, do not
   re-open the baseline grid, and do not promote anything from the child.
3. **The next mutation** (if one is started) has to be a new single-variable
   change of the *baseline* rule, and it has to be run through the corrected
   legs — `scripts/run_mutation_grid.py --resume` semantics, then
   `mutation_eval` → `mutation_repro_check` → `mutation_survivor_check` →
   `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan` — with the
   child's own null as the yardstick, not the parent's.

**Do not** start a second worker on any run directory, do not re-run the
baseline grid, do not change `results/20261019_135940_grid`, and do not
contact the market-data provider before 2026-10-22T11:41:20Z.
