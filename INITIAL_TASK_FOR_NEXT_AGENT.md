**Session 2026-10-22T05:47Z.** Read `NEXT_AGENT_TASK.md` first, then `universe/last_scan.json` and `results/mutations.json`.

**This session (offline only, no provider call):** re-ran `scripts/refresh_universe.py plan` at 2026-10-22T05:33Z — `refresh_allowed_now: false`, the bound 2026-10-22T11:41:20Z has not elapsed. The `state` phase was re-run offline at 05:47:25Z: N=266, floor `AGLD/USDT` $16 279 472, 17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0 symbols without a fixture or grid cells, `next_eligible_refresh_at` unchanged. **No fetch was performed and no provider was contacted.**

**State.**
- The baseline grid `results/20261019_135940_grid` (266 symbols × 66 pairs = 17 556 cells, 0 blocked, verified against the artifact tree) stays the program's grid. The child `results/20261021_172619_grid` is a **closed** negative result (ATR min-risk mutation, `NOT_PROMOTED`); do not re-open it.
- Universe N = 266, floor `AGLD/USDT` $16 279 472, frozen snapshot `universe/mcap_snapshot_20261021_114120.json` (scanned 2026-10-21T11:41:20Z). **Next eligible refresh: 2026-10-22T11:41:20Z.**
- Tests: `232 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T05:47Z). Env: numpy 2.5.4, pandas 3.0.6, pytest 9.1.1 in the user site-packages.

**What this session changed (offline, no provider call).**
- **Defect fix — a failed probe no longer rejects a name.** `scripts/fetch_mcap_snapshot.py:has_min_history` answered a failed probe exactly like a proven absence of history (both `False`), so a transient KuCoin error wrote `insufficient_hourly_history_for_grid` and dropped a tradable name from the eligible set for good. The probe now answers `True` / `False` / `None`; `None` means *unknown*, the name stays a candidate, the fixture download is the authoritative gate (PROMPT.md §2.1.5: an API failure is not proof of ineligibility). `scripts/refresh_universe.py` records the failed names (`history_probe_failures`) and writes `INCOMPLETE_SCAN` instead of an exhausted band for such a pass.
- **The next ranking pass reaches twice the depth.** The 10-page pass of 2026-10-21 covered 1 000 entries down to $15 931 465 — a band of only **ten** names below the floor ($16 279 472), and all ten are ineligible, so the expansion had nothing to select. `scripts/refresh_universe.py` now fetches **20 pages** (2 000 entries) by default; the selection still takes the highest-cap eligible names below the floor, but the band is wide enough to hold candidates. Cost: ~10 min for the pass (the 10-page pass took under 4 min).
- **End-to-end test of the whole cycle** (`fetch → fixtures → grid → state → log`, providers mocked): the append-only ranking, the fixture + manifest rows, 66 cells per new symbol, the waiting state with its 24 h bound, and the expansion-log entry.
- `universe/last_scan.json`: only `last_verified_at`, `last_verification_note`, `coverage_reaches_below_current_floor` and `history_probe_failure_count` changed. The snapshot linkage, the state, `universe_n`, the floor and `next_eligible_refresh_at` are untouched.

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
   `all` runs the five phases in order. `fetch` freezes `universe/mcap_snapshot_<TS>.json` and appends the batch to `universe/mcap_rank.json` append-only in descending market-cap order; `fixtures` fetches hourly KuCoin bars for the **new** names only (target 22 000 bars, integrity-checked) and removes a name again if its bars do not pass the checks; `grid` expands the baseline grid through the repository's own resume path, one symbol at a time; `state` verifies the cells and rewrites the scan record.
   Time budget: fetch ~10 min, fixtures ~2.5 min per name, grid ~1.7 min per name (66 cells × ~1.6 s), pooled legs ~6 min, tests ~1.5 min.
2. **If no name is eligible below the floor**, the band is exhausted: record that in `universe/last_scan.json` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`) and wait for the next 24 h refresh. Do not treat it as a program stop (PROMPT.md §2.1.5). **If the pass reports failed history probes** (state `INCOMPLETE_SCAN`), the band is not exhausted and one early re-pass is allowed: `fetch --override-gate --override-reason "history probes failed on the previous pass"`.
3. **After the expansion:** re-run the pooled legs offline —
   `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid` and
   `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid` —
   then update `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6) and the handoff.
4. **Run `PYTHONPATH=. python3 -m pytest tests/ -q` after any code change** (232 passed at 2026-10-22T05:47Z).
5. **After the expansion**, the next research step is a *new* single-variable mutation of the expanded baseline, run through the corrected legs (`run_mutation_grid.py --resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` → `oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan`) with the **child's own null** as the yardstick, not the parent's. The closed ATR mutation stays closed.

**Operational warning.** The `background_process` **monitor** action *starts* the command it is given — it is not a way to follow a process that is already running. Using it on the verification run of an earlier session started a second copy of the same command; it was stopped within seconds and the check is read-only with respect to the grid, so nothing was affected. Use `background_process start` and then `logs`/`status` to follow a running process.
