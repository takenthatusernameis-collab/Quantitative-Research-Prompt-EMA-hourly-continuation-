# AUTHORIZED MAINTENANCE UPDATE — 2026-10-21

This update was authorized by the user after three refinements of the execution prompt and a completed 120-second terminal wait. The full, versioned instructions are in MAINTENANCE_EXECUTION_BRIEF_20261021.md. Refresh live state before acting; the values here are a saved baseline only.

## Highest-priority task after safely reconciling the current worker

1. Inspect the live status of Actions runs #21 and #22, current job logs if available, results/mutations.json, and the child run results/20261021_172619_grid. Do not cancel, rerun, dispatch, or start a competing writer.
2. The last saved child checkpoint at 2026-10-21 19:11:47 UTC contained 2,999 of 17,556 expected cells and pointed to INJ/USDT (P_fast=34, P_slow=89); stopped=true, stop_reason=in_progress, all_symbols_processed=false. Resume the same child only if ownership and idempotent resume are verified.
3. The saved mutation report is a 24-symbol partial comparison; it has 0 candidates passing the full gates. Do not treat it as the completed 266-symbol validation or alter the baseline.
4. Complete and validate the existing 266 × 66 child grid, compare parent and child on the same full universe, and run the exact acceptance gates, walk-forward, cost stress, selection/null, concentration, and reproducibility checks in the maintenance brief. Keep negative findings negative.
5. Do not refresh market-cap rankings before 2026-10-22 11:41:20 UTC unless a later permitted time is verified from current state. No new candle fetches, no new Actions runs, and no workflow edits.
6. Update the task handoff only with exact evidence: current HEAD, run URLs/status, completed/expected cell counts, missing/duplicate artifacts, test commands/exit codes, report hashes, conclusions, and blockers. Distinguish execution state from economic results.

## Wait-state policy

When waiting for an eligibility timestamp or an external gate, do no repeated provider polling and do not burn sessions retrying a known failure. Perform independent offline validation from already saved artifacts, or stop with an exact wait state and next permitted time. Never claim a task is complete from a commit, checkpoint counter, or workflow badge alone.

---

## Current state (verified against saved artifacts, 2026-10-21T19:40Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** The 24 h market-cap refresh bound is still closed: the last snapshot was taken at **2026-10-21T11:41:20Z** (`universe/mcap_snapshot_20261021_114120.json`, CoinGecko `/api/v3/coins/markets`, 10/10 pages, 1 000 entries) and **no ranking query may be made before 2026-10-22T11:41:20Z**. The universe is unchanged at **N = 266** and the baseline grid is untouched.

- Universe: **N = 266**, floor **AGLD/USDT** $16 279 472. Coverage: 10/10 pages, 1 000 entries, lowest covered rank 1 000 ($15 931 465) - the pass does reach below the floor.
- The below-floor band holds 10 names and **all 10 are excluded**: ELSA, MIRA, TUT, US -> `insufficient_hourly_history_for_grid` (probed directly on KuCoin: live pairs, listed after 2024-10-20); USDM, PIPPIN, M87, ARARA, STKRI, DRB -> `no_tradable_kucoin_spot_usdt_pair`.
- Grid: **17 556 / 17 556 cells complete** in `results/20261019_135940_grid/` (266 symbols x 66 EMA pairs); 0 blocked. Re-verified this session by walking the artifact tree: `progress.json` reports `next_cell: null`, `all_symbols_processed: true`, `n_symbols x n_pairs == completed_cells` (266 x 66 = 17 556), 266 symbol dirs, 17 556 cell summaries, 17 226 gzip + 330 legacy blotters, 0 missing, 0 blocked.
- Decision count: **17 530 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4993**, median **0.5205**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades).
- Cells with full-sample net PF > 1: **36 / 17 556 (0.2%)**. All 36 failed OOS + 2x-cost checks.
- Latest candidate-check artifact: `results/20261021_033219_candidate_check/summary.md` (36 cells, 36 rejected). Latest grid-wide OOS audit: `results/20261021_033523_oos_grid_scan/summary.md` (0 credible candidates out of 17 556 cells).

**Machine-readable state:** `universe/last_scan.json` - `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `AGLD/USDT` $16 279 472, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-22T11:41:20.375553+00:00`. **Do not refresh before 2026-10-22T11:41:20Z** - the 24h refresh bound applies.

## Leg 1 (2026-10-21T10:31Z) - cost-drag decomposition

`scripts/cost_drag_leg.py` explains *why* the grid loses money. Artifact: `results/20261021_102500_cost_drag_leg/`.

- 17 491 cells decomposed on the out-of-sample window: pooled **gross** PF 0.8877 vs pooled **net** PF 0.5298; costs 17 840 159 against a gross P&L of -3 997 685 (cost share 26.6 %).
- Mechanism: the cost of a trade as a share of its gross P&L is `2 * cost_per_side / risk_pct`. The median cell's stop distance is 0.912 % of the entry price, which predicts 26.3 % of the gross P&L in costs against a measured 26.4 %. **The cost of the rule is set by the width of the stop, not by the number of trades.**
- **2 387 cells** would show PF > 1 with no cost at all; only **77** do under the registered cost model. 3 735 cells lose more than half their gross P&L to fees and slippage.
- Sizing legs on 200 re-run cells (200/200 reproduce the stored grid summary exactly): `base` mean net PF 0.2281, `uncapped` 0.2091 (the notional cap binds on 2.6 % of trades), `atr_min_risk` 0.5460 on 17 929 trades instead of 75 005. The PROMPT.md §5.2 ATR minimum-risk mutation buys back the cost drag, it does not create an edge, and it thins the sample.

## Leg 2 (2026-10-21T11:11Z) - the surviving cells against their own randomizations

`scripts/null_grid_scan.py --survivors-from` re-randomizes individual cells many times: is a surviving cell distinguishable from noise *on its own*? Artifact: `results/20261021_104104_null_survivor_scan/`.

- Survivor set: the 10 cells of `results/20261021_033523_oos_grid_scan` with an out-of-sample net PF > 1 **and** still > 1 under 2x costs (BRETT P8_200; GRT P8_200, P20_200; MERL P8_200; DEXE P12_200, P20_200, P21_200, P26_200, P50_200, P55_200). 12 ordinary cells were re-randomized as controls. 60 replicates per cell, 3 null modes, harness re-run on 24 random cells: 24/24 reproduce the stored grid summary.
- **Result: 0 of 10 survivors keep their out-of-sample net PF at a Bonferroni-corrected level over the 17 556 tests the program ran.** Uncorrected p-values are 0.0164-0.0492 - exactly what 10 cells picked out of 17 556 by chance look like. The null's own gate pass rate (block 21 cells, timing 7) is as large as the real rule's 6.
- The grid leg was not recomputed: the three null modes already in `results/20261021_073300_null_grid_scan/cells.jsonl` were copied into the new artifact and the run resumed on them.

## Leg 3 (2026-10-21T12:16Z) - survivor selection audit

`scripts/survivor_selection_audit.py` (new) closes the two selection-bias questions that were still open about the 10 gate survivors. Artifact: `results/20261021_121629_survivor_selection_audit/` (`summary.md`, `summary.json`, `config.json`, `cells.jsonl` = per-cell fold statistics for all 17 556 cells).

```
PYTHONPATH=. python3 scripts/survivor_selection_audit.py \
  --run results/20261019_135940_grid \
  --oos-audit results/20261021_033523_oos_grid_scan
```
(`--render-only <dir>` re-renders `summary.md` from a saved `summary.json`; the leg takes ~2.5 min and reads only the grid blotters - no market data is fetched.)

- **Leg 1 - the family:** the 10 gate survivors sit on 4 symbols (DEXE 6 cells / 66.5 % of the family net P&L, GRT 2, BRETT 1, MERL 1); pooled OOS net PF **1.3353**, **1.1183** under 2x costs. The exact backtest re-run of every family cell reproduces the OOS audit numbers exactly.
- **Leg 2 - leave-one-symbol-out:** the family keeps a pooled net PF above 1 without any single symbol, but re-selecting the family from the remaining cells keeps only **4-7 of the original 10** and **none of the newcomers clears the cost-stress gate** (W P12_200, GMT P8_200, DEXE P100_200, IMX P26_200/P34_200, PUFFER P21_144, SYN P20_200 - all below 1 under 2x costs). Without DEXE the re-selected family fails the pooled 2x-cost gate (0.9680).
- **Leg 3 - walk-forward re-selection over the whole grid:** the full sample of every symbol is cut into 5 sequential folds; at step k the best cell is chosen on the history (folds 1..k, >= 20 trades) and scored on fold k+1, which the selection never saw. Over **1060 steps and 95 786 out-of-fold trades the pooled out-of-fold net PF is 0.6409** (0.4521 under 2x costs); only **8.1 %** of the out-of-fold windows land above PF 1 (2.9 % under 2x costs). Median in-fold net PF of the selected cell 0.8272 -> median out-of-fold net PF **0.6217**.
- **Leg 3b - the selection against the grid's own null** (no randomization needed: the grid holds 17 556 draws of what a cell scores on a fold it was not selected on): the null's share of folds above PF 1 is 1.2-3.3 %, its median PF 0.41-0.55; the selected cells rank at a median of the **0.7768 percentile** and 198 of 1057 beat the null p95 (one-sided exact binomial p 1.9e-57). **The selection does rank the cells; it never ranks one into a net-profitable window.**
- **Leg 4 - sub-period stability:** the out-of-sample window of the 6 closest survivors (BRETT P8_200, DEXE P50_200/P55_200, GRT P20_200, MERL P8_200, ZEN P12_200) is cut into 4 sequential sub-periods; **0 of 6** keep a net PF above 1 in every sub-period that carries trades (the sub-periods are thin: median 22 trades).

## Leg 4 (2026-10-21T17:26Z, still running) - the ATR minimum-risk mutation grid

The PROMPT.md §5.2 mutation is running as a **full 17 556-cell child grid** of the baseline, in the background, 4 workers:

```
PYTHONPATH=. python3 scripts/run_mutation_grid.py --run results/20261021_172619_grid \
  --min-risk-atr --workers 4 --parent-run results/20261019_135940_grid \
  --note "PROMPT.md 5.2 ATR minimum-risk mutation ..."
```
(`scripts/run_mutation_grid.py` drives the *same* engine as `scripts/run_grid.py` with a process pool; a cell whose `summary.json` exists is skipped, so the run is resumable and `progress.json` names the next unprocessed cell. The baseline grid is never re-run through it and never overwritten by it.)

- Parent `results/20261019_135940_grid` -> child `results/20261021_172619_grid`, registered in `results/mutations.json` (`C_min_risk_atr`, config delta `min_risk_atr: false -> true`, `atr_threshold` 1.0, everything else identical).
- **Progress at 2026-10-21T19:50Z: 4 026 / 17 556 cells (61 of 266 symbols) complete**, `next_cell` STRK/USDT P8_12, 0 blocked, ETA **~2026-10-22T01:00Z** at ~40 cells/min (the symbols are processed in market-cap descending order, so the completed ones are the largest names). The process is alive (`ps`: `run_mutation_grid.py --run results/20261021_172619_grid`); **do not start a second instance.**
- **Partial evaluation** (57 symbols): artifact `results/20261021_194500_mutation_eval_partial/`, produced by
  `PYTHONPATH=. python3 scripts/mutation_eval.py --parent results/20261019_135940_grid --child results/20261021_172619_grid --yardstick results/20261021_121629_survivor_selection_audit/summary.json --out results/<TS>_mutation_eval_partial`
  (this also appends the evaluation to `results/mutations.json`; `--mutation-record ''` disables that).
  Trades 3 097 113 -> 1 349 555 (-56.4 %), pooled net PF 0.4864 -> 0.7498, cost share of the gross profit 67.8 % -> 28.9 %, pooled OOS net PF 0.5207 -> 0.7041 (0.3087 -> 0.5015 under 2x costs), **cells clearing the §3.4 gate 0 -> 19**, walk-forward 0.6186 -> 0.7509 (0.4177 -> 0.5705). The child's **own null moves with it** (null median PF 0.4139 -> 0.7274, the selected cells rank at the 0.5249 percentile of that null, one-sided binomial p 0.1068), so the improvement is a cost effect (fewer, wider trades), not a new edge.
  **The child now produces gate-clearing cells, so read Leg 7 before treating any of them as a candidate.**
- **The yardstick is the parent's full-grid walk-forward**: pooled out-of-fold net PF **0.6409** (0.4521 under 2x costs) over 1060 steps and 95 786 out-of-fold trades, from the Leg 3 audit. The child has to beat that on its own symbol set to be worth anything.

## Leg 5 (2026-10-21T19:02Z) - the selection granularity leg

`scripts/selection_granularity_leg.py` repeats the Leg 3 walk-forward with a coarser selection and adds a random control. Artifact: `results/20261021_193200_selection_granularity/` (the earlier `results/20261021_192000_selection_granularity/` is the same run without the 266-symbol family; the two independent invocations agree bit for bit on every shared number, so the script is deterministic).

- Leg A reproduces the audit's Leg 3 exactly: 1060 steps, 95 786 out-of-fold trades, pooled out-of-fold net PF **0.6409** (0.4521 under 2x costs), 8.1 % of the out-of-fold windows above PF 1.
- Leg B - one selection per market-cap family instead of one per symbol: top 5 -> 0.5401, top 10 -> 0.5816, top 25 -> 0.6312, top 50 -> 0.6354, top 100 -> 0.6546, all 266 -> **0.6649** (0.4818 under 2x costs) on 81 254 trades, 0 windows above PF 1.
- Leg C - the random control (a random eligible cell at every step, 200 replicates, seed 20261021): median pooled out-of-fold net PF **0.5601** (p05 0.5529, p95 0.5688). The per-symbol selection sits at the **100th percentile** of that control.
- **Reading:** the selection beats a random pick out of fold and the result survives the coarser selection, so the out-of-fold number is a property of the procedure, not of the selection granularity - and it stays below 1 either way.

## Leg 6 (2026-10-21T19:32Z, new) - the mutation reproduction check

`scripts/mutation_repro_check.py` (new) re-runs sampled cells of *both* runs through the real backtest on the same fixtures and compares them with the stored artifacts, trade by trade. Artifact: `results/20261021_193500_mutation_repro_check/`.

```
PYTHONPATH=. python3 scripts/mutation_repro_check.py --parent results/20261019_135940_grid \
  --child results/20261021_172619_grid --sample 12 --out results/<TS>_mutation_repro_check
```

- **12/12 child cells and 12/12 parent cells reproduce the stored blotter and the stored summary exactly** (max absolute metric delta 0 on trade_count, net/gross PF, Sharpe, max drawdown, equity reconciliation). Both grids are artifacts of the same engine.
- The same leg measures what the filter does to the *path*: the ATR filter skips an entry, so the position state, the equity path and the size of every later trade change with it. Per cell the child drops 86-1 862 of the parent's entry bars and enters at 5-49 bars the parent never took; the first divergence is at bar 21-2 938. **The child is a different trading path, not a pruned copy of the parent's trades** - so the parent -> child -> delta is a comparison of two strategy instances, not of a filtered view of one.
- A defect was found and fixed in `scripts/mutation_eval.py`: the summary-vs-blotter consistency counter was written into the parent's summary for both runs, so the child's own check never ran. It is now a separate function (`count_pf_mismatches`) with a test. The verdict generator was fixed as well (it claimed that no cell clears the gate even when the child produces 19); the evaluation and the survivor check also got a `--render-only` mode, so a `summary.md` can be re-rendered from a saved `summary.json` without recomputing the legs.

## Leg 7 (2026-10-21T19:45Z, new) - the child's gate-clearing cells

`scripts/mutation_survivor_check.py` (new) reads the cells of the child grid that clear the §3.4 gate out of sample and tests them. Artifact: `results/20261021_200500_mutation_survivor_check/` (61 symbols, 4 026 cells).

```
PYTHONPATH=. python3 scripts/mutation_survivor_check.py --child results/20261021_172619_grid \
  --out results/<TS>_mutation_survivor_check
```

- **This is the first family in the program that clears the gate out of sample**: 20 of 4 026 child cells (0.50 %) clear it, on 7 symbols (ENA 5, POL 5, APT 5, WLD 2, RENDER 1, AERO 1, PYTH 1), pooling to an out-of-sample net PF of **1.2606** over 1 633 out-of-sample trades. The parent grid never produces a gate-clearing cell (0 of 17 556) - the mutation buys back the cost drag, and with it the *possibility* of clearing the gate.
- **The family is not one symbol**: the leave-one-symbol-out pooled out-of-sample PF stays between 1.2177 and 1.2765 without any symbol (unlike the parent's DEXE-dependent family).
- **The family is mostly a time artefact**: only **3 of the 20** keep a net PF above 1 in every out-of-sample sub-period that carries trades (POL/USDT P8_200, P21_200, P34_200).
- **The procedure cannot find these cells**: the child's own cells put 4.5 % of their out-of-sample scores above PF 1, and the walk-forward selection on the child grid ranks at the 0.5249 percentile of the child's own null (one-sided binomial p 0.1068).
- **The open leg is the randomized null on the child grid** - do the 20 cells beat their own randomizations, with a Bonferroni correction over the 17 556 cells the child grid tests? Until that leg is run, nothing here is a candidate and the baseline grid stays the program's grid.

## Defect note for whoever writes the next tooling

The artifact layout is **not uniform**: the grid runner writes `trades.csv.gz`, but the five largest market-cap names (BTC, ETH, SOL, BNB, XRP - ranks 1-5) still carry the legacy baseline-study layout `trades.csv` (uncompressed). Their configs are identical and their cells reproduce exactly, but **any tool that assumes the gzip layout silently skips 330 cells - the whole top of the universe.** `scripts/oos_grid_scan.py:read_trades` handles both; reuse it (the new legs do).

## Required next action

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, grid `progress.json` and the latest candidate-check / OOS-audit / null / selection-audit artifacts. Do not repeat completed scans/cells. Verify grid state is self-consistent (`n_symbols x n_pairs == completed_cells`, `all_symbols_processed=true`, `next_cell=null`).

2. **Before 2026-10-22T11:41:20Z:** State is `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Do not force expansion, do not query CoinGecko, and do not relax the gates. Use the wait for offline verification work only.

3. **Monitor the mutation child grid** (`results/20261021_172619_grid/progress.json`). Do not start a second runner instance. When it reports 17 556 / 17 556 cells and `all_symbols_processed: true`:
   - run the full evaluation
     `PYTHONPATH=. python3 scripts/mutation_eval.py --parent results/20261019_135940_grid --child results/20261021_172619_grid --yardstick results/20261021_121629_survivor_selection_audit/summary.json --out results/<TS>_mutation_eval`
     (it updates `results/mutations.json` with the parent -> child -> delta record and the evaluation list),
   - re-run the reproduction check on the full child
     `PYTHONPATH=. python3 scripts/mutation_repro_check.py --parent results/20261019_135940_grid --child results/20261021_172619_grid --sample 24 --out results/<TS>_mutation_repro_check`,
   - re-run the survivor check on the full child
     `PYTHONPATH=. python3 scripts/mutation_survivor_check.py --child results/20261021_172619_grid --out results/<TS>_mutation_survivor_check`,
   - **run the randomized null on the child grid** - this is the leg that decides the child's gate-clearing cells. Model it on the parent's null leg (`scripts/null_grid_scan.py --survivors-from`, the artifact `results/20261021_104104_null_survivor_scan/`): re-randomize every gate-clearing child cell many times (timing / block / sign nulls) and compare with the Bonferroni-corrected level over the 17 556 cells the child grid tests. The parent's version: 0 of 10 survivors survived the correction.
   - compare the child's walk-forward against the parent's yardstick (0.6409 / 0.4521) **on the same 266 symbols**, and record the decision in `results/mutations.json`, `results/RESEARCH_CONCLUSION.md` and `results/FINAL_DECISION.md`. The baseline grid stays the program's grid unless the child clears the §3.4 gate (net OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades, net PF > 1 under 2x costs in the full sample and in the OOS window) **and** beats its own randomizations **and** holds up in the walk-forward.

4. **From 2026-10-22T11:41:20Z, fetch a fresh snapshot.** Use `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run). The script prints a WARNING when the coverage band stops above the floor - if that happens, extend the page count until the coverage reaches below AGLD/USDT $16 279 472, then re-run. Inspect the timestamped snapshot and the per-name exclusion reasons, then apply eligible names strictly below the floor in descending market-cap order.

5. **For any newly eligible names:** fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run the full 66-pair grid per symbol resuming from `results/20261019_135940_grid`, re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py` and `scripts/robustness_pooled.py`, re-run `scripts/oos_grid_scan.py` over the whole grid (it must be re-run after every expansion, not just once), update `universe/mcap_expansion_log.md`, `universe/last_scan.json` and this handoff.

6. **After an expansion, re-run the new selection audit too** - it is the leg that says whether the *procedure* still finds anything:
   `PYTHONPATH=. python3 scripts/survivor_selection_audit.py --run results/20261019_135940_grid --oos-audit <new oos audit dir>`
   (the family of gate survivors is read from the OOS audit artifact, so the OOS audit must be re-run first). The selection-granularity leg (`scripts/selection_granularity_leg.py`) can be re-run on the same grid afterwards.

7. **If the mutation grid is still running and there is spare time**, the priority is the *randomized null on the child grid* (item 3) - it is the leg that decides the child's gate-clearing cells, and it is expensive, so it can be started as soon as the child grid has enough symbols to make the family stable. A *second* pre-registered mutation (PROMPT.md §5 has the ordered list) is lower priority: it needs its own full child grid, so only start one if the wall clock allows it, and record it in `results/mutations.json` first. Do not modify the baseline grid.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results.
- Never promote without OOS + 2x-cost gates (plus subperiod leg).
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

**Python environment note:** the runner image ships no scientific stack. `python3 -m pip install --disable-pip-version-check --no-input numpy pandas pytest requests` is needed before the scripts or the test suite will import. CoinGecko page 6 reliably answers 429; the built-in backoff (5s/10s/20s/40s) recovers it, so budget ~5 minutes for a 10-page ranking pass and run it in the background rather than under a 5-minute timeout.

- 2026-10-21T19:52Z - Prior agent task completed by current session. Reconciled state (grid self-consistent: 266 x 66 = 17 556 cells, all_symbols_processed=true, next_cell=null, 0 blocked, 266 symbol dirs, 17 226 gzip + 330 legacy blotters, 0 missing; universe unchanged N=266, floor AGLD/USDT $16 279 472, eligible_unseen_below_floor_count=0; refresh bound closed until 2026-10-22T11:41:20Z; **no CoinGecko query, no change to the baseline grid or the universe**). Monitored the running mutation child grid (4 026/17 556 cells, 61 symbols, ETA ~2026-10-22T01:00Z) and added two legs for it: the **mutation reproduction check** (`scripts/mutation_repro_check.py` + `tests/test_mutation_repro_check.py`, artifact `results/20261021_193500_mutation_repro_check/`: 12/12 child cells and 12/12 parent cells reproduce their stored blotters and summaries exactly, and the ATR filter changes the trading path - the child enters at bars the parent never took - rather than pruning the parent's trade list) and the **survivor check of the child's gate-clearing cells** (`scripts/mutation_survivor_check.py` + `tests/test_mutation_survivor_check.py`, artifact `results/20261021_200500_mutation_survivor_check/`: the child grid produces the program's first out-of-sample gate-clearing family - 20 of 4 026 cells on 7 symbols, pooled OOS net PF 1.2606 over 1 633 OOS trades, leave-one-symbol-out 1.2177-1.2765 - but only 3 of 20 are stable in every OOS sub-period and the walk-forward selection does not beat the child's own null, 0.5249 percentile, p 0.1068; **the randomized null on the child grid is the open leg**). Fixed two defects in `scripts/mutation_eval.py` (the summary-vs-blotter mismatch counter was written into the parent's summary for both runs, so the child's own check never ran; the verdict claimed that no cell clears the gate even when the child produces 19) and added `--render-only` to the mutation evaluation and the survivor check. Verified the inherited selection-granularity leg (`results/20261021_193200_selection_granularity/`: Leg A reproduces the audit's 0.6409 / 0.4521 exactly; the two independent invocations agree bit for bit). Tests: `python -m pytest tests/ -q` -> 193 passed. State remains AWAITING_NEW_ELIGIBLE_CANDIDATES. Handoffs updated for the next agent.
