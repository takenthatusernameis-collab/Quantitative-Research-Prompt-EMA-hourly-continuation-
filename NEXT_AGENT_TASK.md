# AUTHORIZED MAINTENANCE UPDATE — 2026-10-21 (resumed, late)

This session resumed prior agent work from durable handoff. Full versioned instructions remain in MAINTENANCE_EXECUTION_BRIEF_20261021.md. Refresh live state before acting; saved values current as of this session.

## Current state (verified 2026-10-21T22:32Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES` (universe refresh blocked until 2026-10-22T11:41:20Z).**
- Universe: N=266 (270 symbols in progress.json invocation; 266 registered), floor AGLD/USDT $16,279,472. Last snapshot 2026-10-21T11:41:20Z. No CoinGecko query before 2026-10-22T11:41:20Z. Eligible_unseen_below_floor_count=0.
- Baseline grid: `results/20261019_135940_grid` — 266×66 = 17,556 cells complete. 0 credible candidates after OOS + 2×-cost checks. Pooled full-sample net PF 0.4993; pooled OOS walk-forward yardstick 0.6409 (0.4521 under 2× costs).

## ATR minimum-risk mutation (child) — still running
- Run: `results/20261021_172619_grid` (parent `results/20261019_135940_grid`), registered as `C_min_risk_atr` (min_risk_atr false→true). 4 workers alive; do not start second runner.
- Progress (2026-10-21T22:32Z): **11,484 / 17,556 cells (65.4%)**. Next cell not yet recorded; progress.json last timestamp 20261021_180500. ETA ~2026-10-22T01:00Z.
- Partial evaluation (57 symbols): child improves pooled net PF 0.4864→0.7498, pooled OOS 0.5207→0.7041 (0.3087→0.5015 under 2×), trades drop 56.4%, cells clearing §3.4 gate 0→19. Walk-forward child 0.7509 vs parent 0.6186 on partial set. Child's own null moves with it (selection percentile 0.5249, p=0.1068).
- Survivor check on partial child (4026 cells): first gate-clearing family — 20/4026 cells on 7 symbols (ENA/POL/APT/WLD/RENDER/AERO/PYTH), pooled OOS net PF 1.2606 over 1633 OOS trades, leave-one-symbol-out 1.2177–1.2765. Only 3/20 stable in every OOS sub-period; walk-forward selection does not beat child's own null (p=0.1068). Randomized null on complete child grid is decisive open leg.
- Defects fixed in scripts/mutation_eval.py. Added --render-only to mutation evaluation and survivor check.
- Reproduction check (12/12 child and 12/12 parent) reproduces stored blotters/summaries exactly.

## Required next action (in order)
1. Monitor mutation grid progress.json. Do not start/cancel/rerun/dispatch Actions or second runner.
2. When complete (17556/17556, all_symbols_processed true, next_cell null): run mutation_eval, mutation_repro_check (sample 24), mutation_survivor_check, randomized null on child (Bonferroni over 17556 cells), walk-forward re-selection on child.
3. Decide promotion per gates.
4. From 2026-10-22T11:41:20Z: fetch fresh snapshot, extend/expand, re-run aggregate/candidate/robustness/oos_grid_scan/survivor_selection_audit.
5. Update handoffs with exact evidence.

## Guardrails
No CoinGecko before 2026-10-22T11:41:20Z. No new candle fetches. No Actions triggers. No competing writer. Append-only. Baseline unchanged unless mutation clears all gates. Run python -m pytest tests/ -q after changes.
