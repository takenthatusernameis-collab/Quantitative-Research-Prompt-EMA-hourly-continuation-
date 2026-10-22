**Session 2026-10-22T06:12Z.** Read `NEXT_AGENT_TASK.md` first, then
`universe/last_scan.json` and `results/mutations.json`.

**This session (offline only, no provider call):** the 24 h refresh bound of
`universe/last_scan.json` opens **2026-10-22T11:41:20Z**, and this session ran
before it. `PYTHONPATH=. python3 scripts/refresh_universe.py plan` →
`refresh_allowed_now: false`; the `state` phase was re-run offline: N = 266, floor
`AGLD/USDT` $16 279 472, 17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0
symbols without a fixture or a grid, `next_eligible_refresh_at` unchanged.
**No fetch was performed and no provider was contacted.**

**State.**
- The baseline grid `results/20261019_135940_grid` (266 symbols × 66 pairs = 17 556 cells, 0 blocked, verified against the artifact tree) stays the program's grid. The child `results/20261021_172619_grid` is a **closed** negative result (ATR min-risk mutation, `NOT_PROMOTED`); do not re-open it.
- Universe N = 266, floor `AGLD/USDT` $16 279 472, frozen snapshot `universe/mcap_snapshot_20261021_114120.json` (scanned 2026-10-21T11:41:20Z). **Next eligible refresh: 2026-10-22T11:41:20Z.**
- Tests: `244 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T06:12Z). Env: numpy 2.5.4, pandas 3.0.6, pytest 9.1.1 in the user site-packages.

**What this session changed (offline, no provider call).** Three defects in
`scripts/refresh_universe.py`, all in the path the expansion runs; the strategy,
the cost model, the grid and the universe are untouched.
- **The state could call an unobserved band exhausted.** `phase_state` judged "the band below the floor is exhausted" from `coverage_reaches_below_floor`, the flag the *ranking pass* wrote against the floor it started from. A batch **lowers** the floor of the universe, so a pass that stopped at the old floor never saw the band below the new one — the record said `AWAITING_NEW_ELIGIBLE_CANDIDATES` while the same record carried `coverage_reaches_below_current_floor: false` and the phase printed the opposite. The exhausted state now also requires the pass to have reached below the **current** floor; otherwise the state is `INCOMPLETE_SCAN` (PROMPT.md §2.1.5).
- **The fixtures phase could re-fetch a symbol the grid already ran.** A symbol whose fixture file was missing but whose 66 cells exist was downloaded again, which moves the bar sequence and makes the stored cells stale. Such a symbol is now skipped and reported as a conflict (`fixture_conflicts` in `universe/last_scan.json`): restore the file from git, do not download it again. It is never dropped from the universe.
- **The expansion log could be written twice.** `phase_log` appended unconditionally, so a re-run after a crash produced two sections for one batch, and the generated heading did not continue the `## Batch N` sequence. The phase is now idempotent (`<!-- expansion-key: <snapshot_id>|<names> -->`) and numbers its section `## Batch <next N> (applied <pass time>) - <names> (N old -> new)`. The next section of `universe/mcap_expansion_log.md` is **Batch 27**.
- Tests: 240 → **244** (4 new regression tests in `tests/test_refresh_universe.py`).

**Constraints.**
- Do **not** contact the market-data provider before **2026-10-22T11:41:20Z** (no polling, no "quick check", no partial refresh). After that timestamp: **exactly one** ranking pass; freeze the new snapshot for the following 24 h.
- Do **not** re-run the baseline grid, do **not** re-open the child grid, do **not** start a second worker on any run directory, do **not** promote anything from the child grid, and do **not** re-fetch the fixture of a symbol the grid already ran (a re-fetch moves the bar sequence and makes the stored cells stale).

**Next task (time-gated) — from 2026-10-22T11:41:20Z.**

0. **Check the clock first:** `PYTHONPATH=. python3 scripts/refresh_universe.py plan`. If the bound has not elapsed, **do not fetch** — verify the state offline and stop cleanly.
1. **Exactly one ranking pass**, then the expansion of the new symbols only:
   ```
   PYTHONPATH=. python3 scripts/refresh_universe.py plan
   PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 20 --batch-size 10
   PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
   PYTHONPATH=. python3 scripts/refresh_universe.py grid
   PYTHONPATH=. python3 scripts/refresh_universe.py state
   PYTHONPATH=. python3 scripts/refresh_universe.py log
   ```
   `all` runs the five phases in order. `fetch` freezes `universe/mcap_snapshot_<TS>.json` and appends the batch to `universe/mcap_rank.json` append-only in descending market-cap order; `fixtures` fetches hourly KuCoin bars for the **new** names only (target 22 000 bars, integrity-checked) and removes a name again if its bars do not pass the checks; `grid` expands the baseline grid through the repository's own resume path, one symbol at a time; `state` verifies the cells and rewrites the scan record; `log` **appends** the expansion to `universe/mcap_expansion_log.md` — it is idempotent, so a re-run is safe.
   Time budget: fetch ~10 min (20 CoinGecko pages + ~1 940 KuCoin probes), fixtures ~2.5 min per name, grid ~1.7 min per name (66 cells × ~1.6 s), pooled legs ~6 min, tests ~1.5 min. If a session dies between two phases, continue with the remaining phases — never with `fetch` again.
2. **Expect `state = EXPANSION_AVAILABLE` after the batch, not `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** The batch lowers the floor of the universe, so the band below the *new* floor is the one that matters; a 20-page pass reaches far below it and the eligible names in it are listed in `universe/last_scan.json` → `eligible_unseen_below_floor`. Take them **from the same frozen snapshot** (no new provider pass, the 24 h bound does not move): `python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply` and then the `fixtures` → `grid` → `state` → `log` phases. Only when the record says `AWAITING_NEW_ELIGIBLE_CANDIDATES` (or `INCOMPLETE_SCAN` **with** `coverage_reaches_below_current_floor: true`) is the band really exhausted — then record it and wait for the next 24 h refresh. Do not treat it as a program stop (PROMPT.md §2.1.5). **If the pass reports failed history probes** (`history_probe_failure_count > 0`, state `INCOMPLETE_SCAN`), the band is not exhausted and one early re-pass is allowed: `fetch --override-gate --override-reason "history probes failed on the previous pass"`.
3. **After the expansion:** re-run the pooled legs offline —
   `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid` and
   `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid` —
   then update `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6, section `## Batch 27`) and the handoff.
4. **Run `PYTHONPATH=. python3 -m pytest tests/ -q` after any code change** (244 passed at 2026-10-22T06:12Z).
5. **After the expansion**, the next research step is a *new* single-variable mutation of the expanded baseline, run through the corrected legs (`run_mutation_grid.py --resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` → `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan`) with the **child's own null** as the yardstick, not the parent's. The closed ATR mutation stays closed.

**Operational warning.** The `background_process` **monitor** action *starts* the command it is given — it is not a way to follow a process that is already running. Using it on the verification run of an earlier session started a second copy of the same command; it was stopped within seconds and the check is read-only with respect to the grid, so nothing was affected. Use `background_process start` and then `logs`/`status` to follow a running process.
