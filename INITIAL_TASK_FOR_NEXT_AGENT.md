# Initial task for the next agent — time-gated universe refresh and expansion

## Situation (verified 2026-10-22T09:45Z, offline only)

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES`. The 24 h market-cap refresh bound opens at **2026-10-22T11:41:20Z**. The current session (09:45Z) is **before** the bound, so it ran offline-only: no provider contact, no fetch, nothing changed.

Verified offline state:
- `PYTHONPATH=. python3 scripts/refresh_universe.py plan` → `refresh_allowed_now: false`
- `PYTHONPATH=. python3 scripts/refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked
- `PYTHONPATH=. python3 scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicates, 0 NaN rows
- `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**

Frozen snapshot: `universe/mcap_snapshot_20261021_114120.json` (fetched 2026-10-21T11:41:20Z, 10/10 pages, 1 000 entries). Coverage reaches $15 931 465, below the floor $16 279 472; the band below the floor holds 10 names, all excluded (insufficient history or no KuCoin spot USDT pair). **0 eligible unseen names below the floor** from this snapshot.

Baseline grid `results/20261019_135940_grid` is complete (266 × 66 = 17 556 cells, 0 blocked). Child run `results/20261021_172619_grid` (ATR min-risk mutation) is closed `NOT_PROMOTED`. The strategy has **0 credible candidates** across all 17 556 cells (see `results/FINAL_DECISION.md`). Per PROMPT.md §2.1, a negative result is not a program stop — keep expanding descending market cap.

## What to do (time-gated)

**Step 0 — check the clock first (offline, safe at any time):**
```bash
PYTHONPATH=. python3 scripts/refresh_universe.py plan
```
If `refresh_allowed_now: false`, verify offline and stop cleanly — do **not** contact the provider. The next session after 11:41:20Z runs Step 1.

**Step 1 — exactly one ranking pass + expansion (only after 2026-10-22T11:41:20Z):**
```bash
PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 20 --batch-size 10
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```
(Or `refresh_universe.py all`.) Guards: `fetch` refuses before `next_eligible_refresh_at` and on a second pass; `fixtures` never re-fetches a symbol the grid already ran; `grid` expands via `--resume` skipping existing cells; `log` is idempotent and writes nothing when the cycle added no name.

- If **no name is eligible below the floor**: record snapshot id, fetch time, page coverage, floor and exclusions in `universe/last_scan.json`; keep `state = AWAITING_NEW_ELIGIBLE_CANDIDATES` with `next_eligible_refresh_at = scanned_at + 24 h`; write nothing to the expansion log.
- If **names remain eligible below the floor** in the same snapshot: apply the remainder from the frozen snapshot (no second provider pass):
  ```bash
  PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply
  PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
  PYTHONPATH=. python3 scripts/refresh_universe.py grid
  PYTHONPATH=. python3 scripts/refresh_universe.py state
  PYTHONPATH=. python3 scripts/refresh_universe.py log
  ```
  The remainder gets its own log section (`## Batch 28`); order stays strictly descending market cap.

**Step 2 — after the expansion:**
```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```
Then update `universe/mcap_expansion_log.md` (new section `## Batch 27` or `## Batch 28`, previous N → new N, rank range, source/date — once) and this handoff. The pooled report is replaced inside the run dir; the baseline 266-symbol numbers stay in `results/mutations.json` → `parent.pooled`.

**Step 3 — next step after the expansion:** a new single-variable mutation of the expanded baseline (not the ATR filter, which stays closed), using `scripts/run_mutation_grid.py` single-variable flags (`--stricter-trend`, `--min-risk-atr`, `--atr-threshold`, `--rr`, `--aggressive-exit`), keeping registered costs, folds, entry/exit semantics and §3.4 gates unchanged, evaluated against the child's own randomized null.

## What must not happen
- No provider call before 2026-10-22T11:41:20Z; no second pass inside the 24 h window.
- No re-run of the baseline grid, no re-opening the child grid, no second worker on any run directory, no promotion from the child grid.
- No re-fetch of a fixture the grid already ran.
- No change to the registered grid, cost model, fill rule, folds, or §3.4 gates.
- Run every command from the repository root. Use `start` + `logs`/`status` for background processes.

## Acceptance checklist
- [ ] Exactly one ranking pass; snapshot committed and linked from `universe/last_scan.json`.
- [ ] Pass covered 20 pages; `pages_fetched == pages_requested`.
- [ ] `universe/mcap_rank.json` grew by exactly the batch, descending market cap, old 266 untouched.
- [ ] Fixture exists for every new symbol with ≥17 520 hourly bars, contiguous grid; `data/fixtures/fetch_manifest.json` has a provenance row.
- [ ] Grid has 66 cells per new symbol: `progress.json` shows `completed_cells = (266+n)×66`, `next_cell = null`, 0 blocked.
- [ ] Fixtures of the 266 existing symbols not re-fetched; `universe/last_scan.json` has no `fixture_conflicts`.
- [ ] `universe/last_scan.json` reports new `universe_n`, new floor, remaining eligible count, `next_eligible_refresh_at = scanned_at + 24 h`.
- [ ] `universe/mcap_expansion_log.md` records the expansion once as `## Batch 27` (or `## Batch 28`). If no name added, log unchanged.
- [ ] `PYTHONPATH=. python3 -m pytest tests/ -q` passes.
