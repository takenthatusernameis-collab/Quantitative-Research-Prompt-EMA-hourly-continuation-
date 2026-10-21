# Authorized Maintenance and Validation Brief — EMA Hourly Continuation

Date: 2026-10-21  
Status: Authorized execution guidance. Refresh the live repository state before acting; saved values below are an audit baseline, not guaranteed to remain current.

## Prompt refinement log

### Pass 1 — focus on the highest-value work
Continue the ATR minimum-risk mutation on the existing 266-symbol, 66-pair hourly EMA grid and decide whether the change merits further consideration.

### Pass 2 — prevent wasted compute and false promotion
The child grid already has a persistent checkpoint. Resume/reconcile that run rather than launch a duplicate. Preserve the parent grid, registered costs, folds, entry/exit semantics, candidate gates, and multiple-testing correction. A better profit factor is not enough if it remains below 1 out of sample.

### Pass 3 — make the task resumable, time-aware, and falsifiable
Require exact progress accounting, run ownership/lock checks, full-universe matched evaluation, independent null/selection checks, regression tests, and a strict no-provider-call window. Treat wait state, execution validity, research conclusion, and economic edge as separate statuses.

## Current evidence to re-check before execution

At the last saved checkpoint:
- Child run: results/20261021_172619_grid.
- Saved progress timestamp: 2026-10-21 19:11:47 UTC.
- Intended universe: 266 symbols × 66 EMA pairs = 17,556 cells.
- Completed cells: 2,999; next cell: INJ/USDT, P_fast=34, P_slow=89.
- progress.json says stopped=true, stop_reason=in_progress, all_symbols_processed=false. The grid is incomplete, not a successful completed run.
- results/mutations.json records child C_min_risk_atr as running.
- Existing mutation evaluation, results/20261021_184500_mutation_eval_partial/summary.md, compares only 24 symbols (1,584 cells), not the full universe.
- On that partial 24-symbol comparison, the ATR minimum-risk mutation improves pooled out-of-sample net PF from 0.4787 to 0.6759 and walk-forward pooled out-of-fold net PF from 0.5942 to 0.7239, but the corresponding 2×-cost metrics remain 0.4585 and 0.5370; zero configurations pass the full acceptance gate.
- The full-baseline walk-forward yardstick across 266 symbols is 0.6409 pooled out-of-fold net PF and 0.4521 at 2× costs.
- New baseline selection-granularity analysis (results/20261021_193200_selection_granularity/summary.md) gives 0.6409 per-symbol OOF PF, 0.6649 for one selected EMA pair across the full market-cap family, versus randomized-selection median 0.5601; both real procedures still lose out of fold.
- At the last Actions check, run #21 was in progress but its API last-update time lagged its start substantially, and run #22 was pending. Re-check actual run/job/log state before deciding whether a worker owns the child output.

Refresh the above from current artifacts and the live Actions API before doing work. Never infer completion from these saved numbers.

## Non-negotiable boundaries

1. Keep the registered baseline untouched. The only child mutation is min_risk_atr=True versus the parent min_risk_atr=False. Preserve the EMA period set {8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}, all 66 fast/slow pairs, hourly data semantics, entry/exit timing, cost model, risk sizing, folds, and acceptance thresholds.
2. Do not replace or edit the parent's 17,556-cell artifacts or reinterpret the partial 24-symbol report as full-universe evidence.
3. Do not promote any candidate, declare an edge, or change the baseline decision without the complete registered gates. No live trading, production release, order placement, leverage change, new shorting, or exchange credentials.
4. No CoinGecko market-cap query before 2026-10-22 11:41:20 UTC, unless a newer, verified repository state explicitly shows a later permitted time. A time-bound universe refresh must not be bypassed. Do not repeatedly poll the provider while waiting.
5. Do not trigger, cancel, rerun, or dispatch GitHub Actions from this task. Do not edit workflow files or create a second workflow. Do not launch a second child grid while an existing worker may be writing its artifacts.
6. Do not fetch new candle data. The mutation grid uses the already persisted fixtures/current run configuration; this task is about finishing and validating the existing experiment, not changing the data source or universe.

## Execution plan

### 1. Reconcile run ownership and exact progress
- Read results/mutations.json, the child run_config.json, progress.json, available per-symbol outputs, current task handoffs, and current GitHub Actions run/job state.
- Recompute expected cell count from the registered symbol list and period pairs.
- Reconcile the completed-cell list with result files and summaries; detect duplicate IDs, missing cells, corrupt outputs, cells marked complete without artifacts, and artifacts not represented in progress.
- Check whether the original worker is active or can still write. If ownership is unclear, do not start another writer. Record the uncertainty and use read-only diagnostics until a safe resume boundary exists.
- Resume the existing run only through the repository's tested resume path after verifying idempotency. Do not reset or forge progress counters. If the script cannot safely resume from the saved manifest/checkpoint, add deterministic tests and correct the resume path before consuming more compute.
- Complete the exact frozen universe only if permitted and resource-feasible: expected 17,556 child cells, with zero missing or unverified cells. If blocked, preserve an explicit partial state and never label the grid complete.

### 2. Evaluate the mutation as a procedure, not a cherry-picked list
After full-grid completion and integrity verification, run a matched parent-versus-child comparison over the same 266 symbols and 66 EMA pairs. Include:
- full-sample net and gross PF, net P&L, trade counts, costs, and cost share;
- trailing-35% out-of-sample net PF, net Sharpe, trade count, and the registered 2×-cost stress;
- sequential walk-forward selection using only data available before each scored fold;
- same-grid parent yardstick and the registered randomized/null controls to measure selection bias;
- symbol/rank concentration, time-slice stability, and an audit of absent/duplicate/invalid cells;
- sampled exact re-runs through the authoritative backtest engine, with numerical tolerances recorded;
- tests proving min_risk_atr is the only changed config field.

A configuration can be called credible only if it passes every current PROMPT.md §3.4 gate, including net out-of-sample PF > 1, positive net out-of-sample Sharpe, at least 30 out-of-sample trades, and net PF > 1 under 2× costs in both the full sample and out-of-sample window, plus the registered selection/multiple-testing controls. Verify the exact live gate text before applying it. Do not weaken the gate if no configuration qualifies.

### 3. Wait-state-aware operations
- If the universe is in AWAITING_NEW_ELIGIBLE_CANDIDATES, do not query providers before the recorded next_eligible_refresh_at. Work on existing offline artifacts, tests, diagnostics, or stop cleanly if no independent task is actionable.
- Distinguish pending from stale or failed Actions runs. Use run timestamps, job status, logs, saved progress timestamps, and artifact changes; no single indicator is conclusive.
- Never cancel a potentially valid writer or start a competing writer to make a run appear active. If the only remaining action requires unavailable Actions permissions, record the exact run URL, permission boundary, and safe recovery command for an authorized operator.
- Do not spend repeated sessions rediscovering an already-recorded blocker. Preserve one precise, evidence-backed next task.

### 4. Regression and full-suite validation
Run from the repository root:
- targeted tests for mutation runner/resume, mutation evaluation, artifact integrity, and wait-state handling (discover exact current test names first);
- python -m pytest tests/ -q;
- the repository's consistency/reproducibility checks for the parent and child summaries;
- git status --short and git diff --stat.

Record exact commands, exit codes, test totals, run IDs, child coverage, and artifact hashes. Do not claim a command ran when this session did not execute it.

## Acceptance criteria

Complete only when:
- the original child grid is reconciled to a verified complete state (or remains explicitly blocked/partial);
- the parent and child are compared on the same 266 symbols and all 17,556 cells, without changing the baseline;
- all required OOS, 2× cost, walk-forward, null/multiple-testing, concentration, and reproducibility legs are accounted for;
- test results and report numbers are regenerated from verified artifacts;
- mutations.json accurately reflects running/completed/blocked status;
- the saved handoff explains the next eligible universe-refresh time and prohibits repeated provider polling;
- the conclusion keeps strategy correctness, execution validity, statistical evidence, and economic profitability distinct.

A negative result is a valid research result. A partial grid or failed worker is an infrastructure state, not evidence for or against the strategy.
