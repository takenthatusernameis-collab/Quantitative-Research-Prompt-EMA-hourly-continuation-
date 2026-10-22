**Session 2026-10-22T06:55Z.** Read `NEXT_AGENT_TASK.md` first, then
`universe/last_scan.json` and `results/mutations.json`.

**This session (offline only, no provider call):** the 24 h refresh bound of
`universe/last_scan.json` opens **2026-10-22T11:41:20Z**, and this session ran
before it. `PYTHONPATH=. python3 scripts/refresh_universe.py plan` →
`refresh_allowed_now: false`; the `state` phase was re-run offline: N = 266, floor
`AGLD/USDT` $16 279 472, 17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0
symbols without a fixture or a grid, `next_eligible_refresh_at` unchanged;
`scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps.
**No fetch was performed and no provider was contacted.**

**State.**
- The baseline grid `results/20261019_135940_grid` (266 symbols × 66 pairs = 17 556 cells, 0 blocked, verified against the artifact tree) stays the program's grid. The child `results/20261021_172619_grid` is a **closed** negative result (ATR min-risk mutation, `NOT_PROMOTED`); do not re-open it.
- Universe N = 266, floor `AGLD/USDT` $16 279 472, frozen snapshot `universe/mcap_snapshot_20261021_114120.json` (scanned 2026-10-21T11:41:20Z). **Next eligible refresh: 2026-10-22T11:41:20Z.**
- Tests: `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T06:55Z). Env: numpy 2.5.4, pandas 3.0.6, pytest 9.1.1 in the user site-packages.

**What this session changed (offline, no provider call).** Two defects in
`scripts/refresh_universe.py`, both in the path the expansion runs; the strategy,
the cost model, the grid and the universe are untouched.
- **The expansion log could write the batch of the previous expansion.** `phase_log` took the names it was about to log from the ranking file's `added_in_this_expansion`, which names the *last* expansion and not the current cycle: a ranking pass that finds no eligible name leaves that field untouched, so the first `log` run of such a cycle appended a **second section for batch 26** (`## Batch 27 ... POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO (N 257 -> 266)`) and consumed the number the next real expansion needs. The phase now takes the names of the current cycle from the scan record (`batch_selected`) and writes **nothing** when the cycle added no name — a cycle that adds nothing is not an expansion, and the scan itself stays recorded in `universe/last_scan.json`. The next section of `universe/mcap_expansion_log.md` is still **Batch 27**.
- **The state phase destroyed the expansion floor.** The scan record stores the path of the frozen snapshot *relative to the repository root*, and the phases resolved it against the working directory of the session. Run from anywhere else, the phase read **no snapshot at all**, computed the floor from an empty ranking and wrote `expansion_floor = {"symbol": null, "market_cap_usd": 0}` (a floor of $0 turns every name of the ranking into a candidate below the floor) and flipped the state to `INCOMPLETE_SCAN`. The snapshot path is now resolved against the repository root (`scripts/refresh_universe.py:snapshot_of`), and an unreadable snapshot keeps the recorded floor instead of overwriting it. The same bug had turned the price-identity check of the `fixtures` phase into a no-op outside the repository root.
- Tests: 244 → **249** (5 new regression tests in `tests/test_refresh_universe.py`).

**Constraints.**
- Do **not** contact the market-data provider before **2026-10-22T11:41:20Z** (no polling, no "quick check", no partial refresh). After that timestamp: **exactly one** ranking pass; freeze the new snapshot for the following 24 h.
- Do **not** re-run the baseline grid, do **not** re-open the child grid, do **not** start a second worker on any run directory, do **not** promote anything from the child grid, and do **not** re-fetch the fixture of a symbol the grid already ran (a re-fetch moves the bar sequence and makes the stored cells stale).
- Run the commands **from the repository root** (the scan record, the ranking, the fixture directory and the grid run are relative paths).

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
   `all` runs the five phases in order. `fetch` freezes `universe/mcap_snapshot_<TS>.json` and appends the batch to `universe/mcap_rank.json` append-only in descending market-cap order; `fixtures` fetches hourly KuCoin bars for the **new** names only (target 22 000 bars, integrity-checked) and removes a name again if its bars do not pass the checks; `grid` expands the baseline grid through the repository's own resume path, one symbol at a time; `state` verifies the cells and rewrites the scan record; `log` **appends** the expansion to `universe/mcap_expansion_log.md` — it is idempotent, so a re-run is safe, and it writes **nothing** when the cycle added no name.
   Time budget: fetch ~10 min (20 CoinGecko pages + ~1 940 KuCoin probes), fixtures ~2.5 min per name, grid ~1.7 min per name (66 cells × ~1.6 s), pooled legs ~6 min, tests ~1.5 min. If a session dies between two phases, continue with the remaining phases — never with `fetch` again.
2. **Expect `state = EXPANSION_AVAILABLE` after the batch, not `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** The batch lowers the floor of the universe, so the band below the *new* floor is the one that matters; a 20-page pass reaches far below it and the eligible names in it are listed in `universe/last_scan.json` → `eligible_unseen_below_floor`. Take them **from the same frozen snapshot** (no new provider pass, the 24 h bound does not move): `python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply` and then the `fixtures` → `grid` → `state` → `log` phases. Only when the record says `AWAITING_NEW_ELIGIBLE_CANDIDATES` (or `INCOMPLETE_SCAN` **with** `coverage_reaches_below_current_floor: true`) is the band really exhausted — then record it and wait for the next 24 h refresh. Do not treat it as a program stop (PROMPT.md §2.1.5). **If the pass reports failed history probes** (`history_probe_failure_count > 0`, state `INCOMPLETE_SCAN`), the band is not exhausted and one early re-pass is allowed: `fetch --override-gate --override-reason "history probes failed on the previous pass"`.
3. **After the expansion:** re-run the pooled legs offline —
   `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid` and
   `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid` —
   then update `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6, section `## Batch 27`, or `## Batch 28` for a second batch from the same snapshot) and the handoff. The pooled report of the 266-symbol baseline is replaced by the expanded one in the run directory; its numbers stay in `results/mutations.json` → `parent.pooled`.
4. **Run `PYTHONPATH=. python3 -m pytest tests/ -q` after any code change** (249 passed at 2026-10-22T06:55Z).
5. **After the expansion**, the next research step is a *new* single-variable mutation of the expanded baseline, run through the corrected legs (`run_mutation_grid.py --resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` → `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan`) with the **child's own null** as the yardstick, not the parent's. The closed ATR mutation stays closed.

**Operational warning.** The `background_process` **monitor** action *starts* the command it is given — it is not a way to follow a process that is already running. Using it on the verification run of an earlier session started a second copy of the same command; it was stopped within seconds and the check is read-only with respect to the grid, so nothing was affected. Use `background_process start` and then `logs`/`status` to follow a running process.
