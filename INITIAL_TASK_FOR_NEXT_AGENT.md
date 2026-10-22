**Session 2026-10-22T05:21Z.** Read `NEXT_AGENT_TASK.md` first, then `universe/last_scan.json` and `results/mutations.json`.

**This session (offline only, no provider call):** re-ran `scripts/refresh_universe.py plan` at 2026-10-22T05:21:50Z — `refresh_allowed_now: false`, bound 2026-10-22T11:41:20Z not elapsed, state unchanged (N=266, floor AGLD/USDT $16 279 472, 0 symbols without fixture/grid cells). No fetch performed. Stop cleanly; the expansion belongs to the session that runs after 11:41:20Z.

**State.**
- The baseline grid `results/20261019_135940_grid` (266 symbols × 66 pairs = 17 556 cells, 0 blocked, verified against the artifact tree) stays the program's grid. The child `results/20261021_172619_grid` is a **closed** negative result (ATR min-risk mutation, `NOT_PROMOTED`); do not re-open it.
- Universe N = 266, floor `AGLD/USDT` $16 279 472, frozen snapshot `universe/mcap_snapshot_20261021_114120.json` (scanned 2026-10-21T11:41:20Z). **Next eligible refresh: 2026-10-22T11:41:20Z.**
- Tests: `223 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T05:20Z). Env: numpy 2.5.4, pandas 3.0.6, pytest 9.1.1 in the user site-packages.

**What this session changed (offline, no provider call).**
- `scripts/refresh_universe.py` (new, 25 tests in `tests/test_refresh_universe.py`): the gated refresh is now one command sequence — `plan` → `fetch` → `fixtures` → `grid` → `state` → `log`. The 24 h bound is enforced **in code**: the `fetch` phase records `next_eligible_refresh_at = scanned_at + 24 h` in the scan record, so a second ranking pass inside the window is refused before any provider call.
- `scripts/fetch_mcap_snapshot.py`: **defect fix.** The ticker-collision resolution looked for the fixture under the base ticker (`ONE.csv`) while a fixture is named after the whole symbol (`ONE_USDT.csv`), so the lookup always failed and an ambiguous ticker fell back to the first ranking entry — the market cap of a *different asset*. Six included symbols are ambiguous (SAFE, VELO, MEME, MASK, ONE, XAI). The recorded floor is unchanged (`AGLD/USDT` $16 279 472), so no stored state was invalidated and no cell has to be re-run.
- **Pre-flight for the expansion:** `results/20261022_052000_baseline_grid_repro` — 300 sampled baseline cells re-run through the real backtest reproduce their stored summary **exactly (300/300, 0 stale)**, so no fixture of the 266 existing symbols has drifted and the expansion only adds cells.
- `universe/last_scan.json`: only `last_verified_at`, `last_verification_note` and a new `grid_verification` block changed (17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0 symbols without a fixture). The `plan` and `state` phases of the new tool were exercised against the real repository; the snapshot linkage, the state, `universe_n`, the floor and `next_eligible_refresh_at` are untouched.

**Constraints.**
- Do **not** contact the market-data provider before **2026-10-22T11:41:20Z** (no polling, no "quick check", no partial refresh). After that timestamp: **exactly one** ranking pass; freeze the new snapshot for the following 24 h.
- Do **not** re-run the baseline grid, do **not** re-open the child grid, do **not** start a second worker on any run directory, do **not** promote anything from the child grid, and do **not** re-fetch the fixture of a symbol the grid already ran (a re-fetch moves the bar sequence and makes the stored cells stale).

**Next task (time-gated) — from 2026-10-22T11:41:20Z.**

0. **Check the clock first:** `PYTHONPATH=. python3 scripts/refresh_universe.py plan`. If the bound has not elapsed, **do not fetch** — verify the state offline and stop cleanly. (The workflow run of this session ends ~2026-10-22T10:26Z, i.e. before the bound; the session that can act is the one that runs after 11:41:20Z.)
1. **Exactly one ranking pass**, then the expansion of the new symbols only:
   ```
   PYTHONPATH=. python3 scripts/refresh_universe.py plan
   PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 10 --batch-size 10
   PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
   PYTHONPATH=. python3 scripts/refresh_universe.py grid
   PYTHONPATH=. python3 scripts/refresh_universe.py state
   PYTHONPATH=. python3 scripts/refresh_universe.py log
   ```
   `all` runs the five phases in order. `fetch` freezes `universe/mcap_snapshot_<TS>.json` and appends the batch to `universe/mcap_rank.json` append-only in descending market-cap order; `fixtures` fetches hourly KuCoin bars for the **new** names only (target 22 000 bars, integrity-checked); `grid` expands the baseline grid through the repository's own resume path, one symbol at a time; `state` verifies the cells and rewrites the scan record.
2. **If no name is eligible below the floor**, the band is exhausted: record that in `universe/last_scan.json` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`) and wait for the next 24 h refresh. Do not treat it as a program stop (PROMPT.md §2.1.5).
3. **After the expansion:** re-run the pooled legs offline —
   `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid` and
   `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid` —
   then update `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6) and the handoff.
4. **Run `PYTHONPATH=. python3 -m pytest tests/ -q` after any code change** (223 passed at 2026-10-22T05:20Z).

**Operational warning.** The `background_process` **monitor** action *starts* the command it is given — it is not a way to follow a process that is already running. Using it on the verification run of this session started a second copy of the same command; it was stopped within seconds and the check is read-only with respect to the grid, so nothing was affected (the same incident is documented in the 2026-10-22 session of `NEXT_AGENT_TASK.md`). Use `background_process start` and then `logs`/`status` to follow a running process.

**If a new mutation is started** (not the pending task): it has to be a new single-variable change of the *baseline* rule, run through the corrected legs — `run_mutation_grid.py --resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` → `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan` — with the **child's own null** as the yardstick, not the parent's.
