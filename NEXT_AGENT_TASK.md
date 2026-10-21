# AUTHORIZED MAINTENANCE UPDATE — 2026-10-21 (resumed)

This session resumed the prior agent's work from the durable handoff. The full versioned instructions remain in MAINTENANCE_EXECUTION_BRIEF_20261021.md. Refresh live state before acting; saved values below are current as of this session.

## Current state (verified 2026-10-21T20:05Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.**
- Universe: N=266, floor AGLD/USDT $16,279,472. Last snapshot 2026-10-21T11:41:20Z. **No CoinGecko ranking query before 2026-10-22T11:41:20Z** (`universe/last_scan.json`: state AWAITING_NEW_ELIGIBLE_CANDIDATES, next_eligible_refresh_at 2026-10-22T11:41:20.375553+00:00). Eligible_unseen_below_floor_count=0.
- Baseline grid: `results/20261019_135940_grid` — 266×66 = 17,556 cells complete (self-consistent). 0 credible candidates after OOS + 2×-cost checks. Pooled full-sample net PF 0.4993; pooled OOS walk-forward yardstick 0.6409 (0.4521 under 2× costs) per Leg 3.
- No changes made to baseline grid or universe this session.

## ATR minimum-risk mutation (child) — still running
- Run: `results/20261021_172619_grid` (parent `results/20261019_135940_grid`), registered in `results/mutations.json` as `C_min_risk_atr` (min_risk_atr false→true). 4 workers alive.
- Progress (2026-10-21T20:05Z): **5016 / 17556 cells (28.6%)**, 76 symbols processed in order, next cell `['LUNC/USDT', 8, 12]`. ETA ~2026-10-22T01:00Z. **Do not start a second runner.**
- Partial evaluation (57 symbols): child improves pooled net PF 0.4864→0.7498, pooled OOS 0.5207→0.7041 (0.3087→0.5015 under 2×), trades drop 56.4% (cost share drops), **cells clearing §3.4 gate 0→19**. Walk-forward child 0.7509 vs parent 0.6186 on that partial set. Child’s own null moves with it (selection percentile 0.5249, p=0.1068).
- Reproduction check (`results/20261021_193500_mutation_repro_check`): 12/12 child and 12/12 parent cells reproduce stored blotters/summaries exactly; ATR filter changes trading path (different entry bars), not a prune of parent trades.
- Survivor check on partial child (`results/20261021_200500_mutation_survivor_check`, 4026 cells): **first gate-clearing family in program** — 20 of 4026 cells on 7 symbols (ENA/POL/APT/WLD/RENDER/AERO/PYTH), pooled OOS net PF **1.2606** over 1633 OOS trades, leave-one-symbol-out 1.2177–1.2765. Only **3/20** stable in every OOS sub-period; walk-forward selection does **not** beat child’s own null (percentile 0.5249, p=0.1068). **Randomized null on the complete child grid is the decisive open leg.**
- Defects fixed in `scripts/mutation_eval.py` (summary-vs-blotter counter scoped to child; verdict corrected when child produces gate-clearing cells). Added `--render-only` to mutation evaluation and survivor check.

## Required next action (in order)
1. **Monitor mutation grid.** Watch `results/20261021_172619_grid/progress.json`. Do **not** start/cancel/rerun/dispatch Actions.
2. **When complete (17556/17556, all_symbols_processed true, next_cell null):** run
   - `PYTHONPATH=. python3 scripts/mutation_eval.py --parent results/20261019_135940_grid --child results/20261021_172619_grid --yardstick results/20261021_121629_survivor_selection_audit/summary.json --out results/<TS>_mutation_eval` (updates `results/mutations.json`)
   - `PYTHONPATH=. python3 scripts/mutation_repro_check.py --parent results/20261019_135940_grid --child results/20261021_172619_grid --sample 24 --out results/<TS>_mutation_repro_check`
   - `PYTHONPATH=. python3 scripts/mutation_survivor_check.py --child results/20261021_172619_grid --out results/<TS>_mutation_survivor_check`
   - **Randomized null on child grid:** `PYTHONPATH=. python3 scripts/null_grid_scan.py --survivors-from <child-oos-audit-dir-or-use-survivors-from-child>` following the parent pattern (`results/20261021_104104_null_survivor_scan/`). Re-randomize gate-clearing child cells (timing/block/sign nulls), Bonferroni-correct over all 17556 child cells tested. Parent had 0/10 survive correction.
   - Walk-forward re-selection on complete child grid via `scripts/survivor_selection_audit.py` against child run + its OOS audit.
3. **Decide promotion:** Only promote if child clears §3.4 gates (net OOS PF>1, net OOS Sharpe>0, >=30 OOS trades, net PF>1 under 2× costs in full sample and OOS), **and** beats its own randomizations (Bonferroni-corrected), **and** holds up in walk-forward vs parent yardstick (0.6409/0.4521). Baseline stays program grid otherwise.
4. **From 2026-10-22T11:41:20Z:** fetch fresh snapshot with `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (background), extend if coverage below floor, expand if eligible names appear, re-run aggregate/candidate/robustness/oos_grid_scan/survivor_selection_audit.
5. **Update handoffs** with exact evidence (HEAD, run status, completed/expected, missing/dupes, test cmds/exits, hashes, conclusion).

## Guardrails
- No CoinGecko before 2026-10-22T11:41:20Z. No new candle fetches. No Actions triggers/cancels/reruns/dispatches. No workflow edits. No competing writer.
- Append-only, market-cap desc, below floor only. Baseline unchanged unless preregistered mutation clears all gates.
- Keep strategy correctness, execution validity, statistical evidence, economic profitability distinct. Negative result is valid.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
- Use `PYTHONPATH=. python3 scripts/...` from repo root. Dependencies may need `python3 -m pip install --disable-pip-version-check --no-input numpy pandas pytest requests`. CoinGecko has backoff; budget ~5 min for 10-page pass.
