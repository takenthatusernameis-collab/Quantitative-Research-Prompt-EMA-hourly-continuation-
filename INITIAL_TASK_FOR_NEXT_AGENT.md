**Session 2026-10-22T08:23Z.** Read `NEXT_AGENT_TASK.md` first, then `universe/last_scan.json` and `results/mutations.json`.

**This session (offline only, no provider call):** 24 h refresh bound opens **2026-10-22T11:41:20Z**. `PYTHONPATH=. python3 scripts/refresh_universe.py plan` → `refresh_allowed_now: false`. `state` re-run offline: N=266, floor AGLD/USDT $16 279 472, 17556/17556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid. Tests: `249 passed`. No fetch, no provider contact.

**State.**
- Baseline grid `results/20261019_135940_grid` stays the program's grid (266×66). Child `results/20261021_172619_grid` closed negative (`NOT_PROMOTED`); do not re-open/promote.
- Universe N=266, floor $16 279 472, frozen snapshot `universe/mcap_snapshot_20261021_114120.json` (2026-10-21T11:41:20Z). Next eligible refresh: **2026-10-22T11:41:20Z**.
- Tests: 249 passed.

**Constraints.**
- Do **not** contact provider before **2026-10-22T11:41:20Z** (no polling/quick check/partial). After: **exactly one** ranking pass, freeze new snapshot for 24 h.
- Do **not** re-run baseline grid, re-open child grid, start second worker on any run dir, promote from child grid, or re-fetch fixture of a symbol grid already ran.
- Run from repository root.

**Next task (time-gated) — from 2026-10-22T11:41:20Z:**
0. Check: `PYTHONPATH=. python3 scripts/refresh_universe.py plan`. If not elapsed, verify offline and stop cleanly.
1. Exactly one ranking pass + expansion (new symbols only):
   ```bash
   PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 20 --batch-size 10
   PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
   PYTHONPATH=. python3 scripts/refresh_universe.py grid
   PYTHONPATH=. python3 scripts/refresh_universe.py state
   PYTHONPATH=. python3 scripts/refresh_universe.py log
   ```
   If pass adds no name, `log` writes nothing and state remains/records `AWAITING_NEW_ELIGIBLE_CANDIDATES` with `next_eligible_refresh_at = scanned_at + 24 h`. If eligible names remain below new floor in same snapshot, apply remainder with `fetch_mcap_snapshot.py --apply-from <snapshot> --batch-size 10 --apply` followed by `fixtures`→`grid`→`state`→`log` (Batch 28). If history probes fail and band not exhausted, one early re-pass allowed with override reason.
2. After expansion: `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`, `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`, update `universe/mcap_expansion_log.md`, update handoff, run tests. Pooled replaces in run dir; parent pooled in `results/mutations.json` unchanged.
3. Next step after expansion: new single-variable mutation of expanded baseline via corrected legs with child's own null as yardstick (ATR mutation stays closed).

**Operational note:** `background_process monitor` starts the command (not for following existing). Use `start` + `logs`/`status`.
