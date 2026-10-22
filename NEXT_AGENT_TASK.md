# NEXT TASK — gated universe refresh and expansion (from 2026-10-22T11:41:20Z)

**Read this file first.** It supersedes the task descriptions of 2026-10-21 and
2026-10-22; the durable record of the closed mutation is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Baseline grid (the program's grid) | `results/20261019_135940_grid` — 266 symbols × 66 pairs = 17 556 cells, complete, 0 blocked |
| Universe | N = 266, floor `AGLD/USDT` $16 279 472 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261021_114120.json` (fetched 2026-10-21T11:41:20Z, 10/10 pages, 1 000 entries, lowest covered $15 931 465) |
| **Next eligible universe refresh** | **2026-10-22T11:41:20Z** (24 h after the snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see §6) |
| Tests | `222 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T05:10Z) |
| New tooling | `scripts/refresh_universe.py` (gated refresh, one command sequence) |

**Provider discipline.** Until 2026-10-22T11:41:20Z the market-data provider must
not be contacted at all — no polling, no "quick check", no partial refresh. After
that timestamp exactly **one** ranking pass is allowed; the new snapshot is then
frozen for the following 24 h. Repeated provider polling is not a way to make
progress here and it is not a task.

**Timing note.** The workflow run that produced this handoff ends at ~10:26Z
(355-minute safety cutoff), i.e. before the bound opens. A session that starts
before 11:41:20Z must not fetch: verify the state offline and stop cleanly. The
expansion belongs to the first session that runs after the bound.

---

## 2. The task

### 2.1 Check the clock (offline, safe at any time)

```
PYTHONPATH=. python3 scripts/refresh_universe.py plan
```

It prints the recorded state, whether a refresh is allowed now and why, and which
symbols still need a fixture or a grid. It never touches the network.

### 2.2 One ranking pass, then the expansion

```
PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 10 --batch-size 10
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```

`all` runs the five phases in order. What each phase does and what it must not do:

| Phase | Effect | Guard |
|---|---|---|
| `fetch` | one CoinGecko pass (`/api/v3/coins/markets`, `order=market_cap_desc`, 10 pages), snapshot frozen to `universe/mcap_snapshot_<TS>.json`, batch appended to `universe/mcap_rank.json` (append-only, descending market cap), scan record written | refuses to run before `next_eligible_refresh_at`; a second pass in the same window is refused before any provider call |
| `fixtures` | hourly KuCoin bars for the **new** symbols only (target 22 000 bars), integrity-checked (bar count, duplicate timestamps, contiguous hourly grid, valid OHLC, price identity), provenance written to `data/fixtures/fetch_manifest.json` | never re-fetches a symbol the grid already ran — that would move the bar sequence and make the stored cells stale (`scripts/verify_grid_repro.py`) |
| `grid` | expands the baseline grid with the new symbols through the repository's own resume path (`scripts/run_grid.py --resume`), one symbol at a time, in descending market-cap order | existing cells are skipped, never recomputed; the run config keeps the history of every invocation |
| `state` | verifies the grid (cells complete, blocked cells, incomplete symbols), recomputes the floor and the names still eligible below it, rewrites `universe/last_scan.json` | writes `state`, `universe_n`, `expansion_floor`, `eligible_unseen_below_floor_count`, `next_eligible_refresh_at` |
| `log` | appends the batch to `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6) | — |

### 2.3 The classic path (only if the new tool misbehaves)

The same work with the older, tested commands — one provider pass, then the
append-only expansion:

```
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply
PYTHONPATH=. python3 scripts/fetch_kucoin.py --symbols <NEW/USDT> [...] --target-bars 22000
PYTHONPATH=. python3 scripts/run_grid.py --resume results/20261019_135940_grid --n <rank> --note "universe expansion: N 266 -> <new N> (<SYMBOL>/USDT, 66-pair EMA grid); snapshot <TS>"
```

`--n <rank>` is the 1-based position of the new symbol in `universe/mcap_rank.json`;
the runner processes the ranking prefix and skips every cell that already has a
`summary.json`. One invocation per symbol keeps `progress.json` consistent after
each symbol.

### 2.4 After the expansion

```
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```

Both legs are offline (they read the artifacts the grid already wrote). Then
update `universe/mcap_expansion_log.md` and this handoff.

### 2.5 If no name is eligible below the floor

The band is exhausted for that snapshot: record the snapshot id, the fetch time,
the page coverage, the market-cap floor and the exclusions in
`universe/last_scan.json`, keep `state = AWAITING_NEW_ELIGIBLE_CANDIDATES` and
set `next_eligible_refresh_at = scanned_at + 24 h`. That is a waiting state, not a
program stop (PROMPT.md §2.1.5): the ranking is refreshed again after 24 h and the
program continues when a new name appears below the floor.

---

## 3. Acceptance checklist for the session that runs the expansion

* [ ] Exactly one ranking pass; the snapshot file is committed and linked from `universe/last_scan.json`.
* [ ] `universe/mcap_rank.json` grew by exactly the batch, in descending market-cap order, with the old 266 symbols untouched and in place.
* [ ] A fixture exists for every new symbol, with ≥ 17 520 hourly bars, and `data/fixtures/fetch_manifest.json` has a provenance row for it.
* [ ] The grid holds 66 cells per new symbol: `results/20261019_135940_grid/progress.json` shows `completed_cells = (266 + n) × 66`, `next_cell = null`, 0 blocked.
* [ ] The fixtures of the 266 existing symbols were **not** re-fetched (their row counts and spans in `fetch_manifest.json` are unchanged).
* [ ] `universe/last_scan.json` reports the new `universe_n`, the new floor, the remaining eligible count and `next_eligible_refresh_at = scanned_at + 24 h`.
* [ ] `universe/mcap_expansion_log.md` records previous N → new N, the rank range added and the ranking source/date.
* [ ] `PYTHONPATH=. python3 -m pytest tests/ -q` passes (222 at the time of writing).

---

## 4. What must not happen

* No provider call before 2026-10-22T11:41:20Z, and no second pass inside the 24 h window afterwards.
* No re-run of the baseline grid, no re-opening of the child grid, no second worker on any run directory, no promotion from the child grid.
* No re-fetch of a fixture the grid already ran (it invalidates the stored cells).
* No change to the registered grid, the cost model, the fill rule, the folds or the §3.4 gates.

---

## 5. Useful facts about the current universe

* The 10 names between the floor and the bottom of the coverage band of the
  current snapshot are all excluded: 4 without two years of hourly history
  (ELSA, MIRA, TUT, US) and 6 without a tradable KuCoin spot USDT pair
  (USDM, PIPPIN, M87, ARARA, STKRI, DRB). The exclusions were probed directly
  against the KuCoin candles API on 2026-10-21T11:44Z, so they are genuine and
  not transient API errors.
* Six included symbols have an ambiguous ticker in the ranking (SAFE, VELO, MEME,
  MASK, ONE, XAI). `scripts/fetch_mcap_snapshot.py` now resolves those against the
  fixture the universe holds (the fix of 2026-10-22T05:05Z); the recorded floor
  is unaffected.
* `data/fixtures/` holds 267 CSV files for 266 ranking symbols (CCD/USDT is a
  pre-fetched file that is not part of the universe).

---

## 6. The closed mutation (context only — do not re-open it)

`results/mutations.json` → `children.C_min_risk_atr`: the PROMPT.md §5.2 ATR
minimum-risk mutation (`min_risk_atr: false → true`, every other config field
identical to the baseline) was run as a single-variable child of the baseline grid
(`results/20261021_172619_grid`, 17 556 cells) and closed as **`NOT_PROMOTED`**:
pooled out-of-sample net PF 0.6676 (0.4781 at 2× costs), 106 gate-clearing cells
against 329 in the child's own timing null, family-wise p 0.9933, walk-forward
selection at the 55.7th percentile of that null, and 0 of 106 survivors above
their own randomization at a Bonferroni-corrected level. The child grid stays as a
documented, reproducible negative result and as the reference point for the next
mutation; the baseline grid was not replaced.

A new mutation, if one is started, has to be a new single-variable change of the
**baseline** rule and has to run through the corrected legs — `run_mutation_grid.py
--resume` → `mutation_eval` (full + repro) → `mutation_survivor_check` →
`oos_grid_scan` → `survivor_selection_audit` → `null_grid_scan` — with the child's
own null as the yardstick, not the parent's.
