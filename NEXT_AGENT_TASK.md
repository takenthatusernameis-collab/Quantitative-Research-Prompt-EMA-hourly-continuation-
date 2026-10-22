# NEXT TASK — gated universe refresh and expansion (from 2026-10-22T06:55Z)

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
| Last offline verification | 2026-10-22T06:55Z — `refresh_universe.py plan` → `refresh_allowed_now: false`; the `state` phase was re-run offline: N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0 symbols without fixture/grid cells, bound unchanged. `progress.json` is in sync with the artifact tree (17 556 cells, 0 stale). `scripts/validate_fixtures.py --all`: 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows. **No provider call.** |
| **Next eligible universe refresh** | **2026-10-22T11:41:20Z** (24 h after the snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see §7) |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`, 2026-10-22T06:55Z) |
| Tooling | `scripts/refresh_universe.py` (gated refresh, one command sequence) — the ranking pass covers **20 pages** and a failed hourly-history probe no longer rejects a name; `scripts/refresh_gate.py` holds the 24 h bound that **both** refresh tools enforce |

**Provider discipline.** Until 2026-10-22T11:41:20Z the market-data provider must
not be contacted at all — no polling, no "quick check", no partial refresh. After
that timestamp exactly **one** ranking pass is allowed; the new snapshot is then
frozen for the following 24 h. Repeated provider polling is not a way to make
progress here and it is not a task.

**Timing note.** A session that starts before 11:41:20Z must not fetch: verify the
state offline and stop cleanly. The expansion belongs to the first session that
runs after the bound.

**Working directory.** Run the commands below **from the repository root**. The
scan record, the ranking, the fixture directory and the grid run are relative
paths; only the frozen snapshot is resolved against the repository root (see
§5.2).

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
PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 20 --batch-size 10
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```

`all` runs the five phases in order. What each phase does and what it must not do:

| Phase | Effect | Guard |
|---|---|---|
| `fetch` | one CoinGecko pass (`/api/v3/coins/markets`, `order=market_cap_desc`, **20 pages** = 2 000 entries), snapshot frozen to `universe/mcap_snapshot_<TS>.json`, batch appended to `universe/mcap_rank.json` (append-only, descending market cap), scan record written | refuses to run before `next_eligible_refresh_at`; a second pass in the same window is refused before any provider call; an override needs `--override-gate --override-reason "<reason>"` |
| `fixtures` | hourly KuCoin bars for the **new** symbols only (target 22 000 bars), integrity-checked (bar count, duplicate timestamps, contiguous hourly grid, valid OHLC, price identity), provenance written to `data/fixtures/fetch_manifest.json` | never re-fetches a symbol the grid already ran — that would move the bar sequence and make the stored cells stale (`scripts/verify_grid_repro.py`). **Since 2026-10-22T06:12Z this is enforced:** a symbol whose 66 cells exist but whose fixture file is missing is skipped and reported as a *conflict* (`fixture_conflicts` in `universe/last_scan.json`) — restore the file from git, do not download it again |
| `grid` | expands the baseline grid with the new symbols through the repository's own resume path (`scripts/run_grid.py --resume`), one symbol at a time, in descending market-cap order | existing cells are skipped, never recomputed; the run config keeps the history of every invocation |
| `state` | verifies the grid (cells complete, blocked cells, incomplete symbols), recomputes the floor and the names still eligible below it, rewrites `universe/last_scan.json` | writes `state`, `universe_n`, `expansion_floor`, `eligible_unseen_below_floor_count`, `next_eligible_refresh_at`; a pass with failed history probes is `INCOMPLETE_SCAN`, never an exhausted band — and, **since 2026-10-22T06:12Z**, neither is a pass that never reached below the *current* floor (§5.1) |
| `log` | appends the batch to `universe/mcap_expansion_log.md` (PROMPT.md §2.1.6) | **idempotent since 2026-10-22T06:12Z** (a repeated run recognises its own batch instead of appending it twice) and the section continues the numbering: the next section is **Batch 27**. **Since 2026-10-22T06:55Z it also writes nothing when the cycle added no name** (§5.2) |

**Time budget** (measured on this repository, 266-symbol baseline):

| Phase | Wall time | Note |
|---|---|---|
| `plan` / `state` / `log` | seconds | offline |
| `fetch` (20 pages) | ~10 min | 20 CoinGecko pages 9 s apart + two KuCoin probes per name with a tradable pair (the 10-page pass took under 4 min; 20 pages probe ~1 940 endpoints, so expect 8–20 min) |
| `fixtures` (10 names) | ~25 min | ~2.5 min per symbol (220 candle requests, 0.4 s apart) |
| `grid` (10 symbols) | ~20 min | 66 cells × ~1.6 s per symbol, plus ~4 s of skipped-prefix loading per invocation |
| `aggregate_grid` + `candidate_check` | ~6 min | offline, reads the cells the grid wrote |
| `pytest tests/ -q` | ~1.5 min | 249 tests |

**If a session dies between two phases**, continue with the remaining phases
(`fixtures` → `grid` → `state` → `log`) — never with `fetch` again: the gate will
refuse it, and the snapshot of the first pass is the one the expansion works on.
The `log` phase can be re-run safely (it is idempotent); the `fetch` phase must
not be.

### 2.3 The classic path (only if the new tool misbehaves)

The same work with the older, tested commands — one provider pass, then the
append-only expansion:

```
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20 --batch-size 10
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply
PYTHONPATH=. python3 scripts/fetch_kucoin.py --symbols <NEW/USDT> [...] --target-bars 22000
PYTHONPATH=. python3 scripts/run_grid.py --resume results/20261019_135940_grid --n <rank> --note "universe expansion: N 266 -> <new N> (<SYMBOL>/USDT, 66-pair EMA grid); snapshot <TS>"
```

`--n <rank>` is the 1-based position of the new symbol in `universe/mcap_rank.json`;
the runner processes the ranking prefix and skips every cell that already has a
`summary.json`. One invocation per symbol keeps `progress.json` consistent after
each symbol.

The classic path now obeys the same 24 h bound as the gated tool (it refuses a
live pass before `next_eligible_refresh_at`, and accepts a written override:
`--override-gate --override-reason "<reason>"`). `--apply-from` makes no provider
call and is therefore never gated.

### 2.4 After the expansion

```
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```

Both legs are offline (they read the artifacts the grid already wrote). Then
update `universe/mcap_expansion_log.md` and this handoff.

Note on the pooled report: `aggregate_grid.py` writes `pooled.md`,
`per_symbol.json`, `per_pair.json` and `summary.json` **inside the run
directory**, so the re-run replaces the 266-symbol report with the expanded one.
The 266-symbol numbers are kept in `results/mutations.json` → `parent.pooled`
(mean net PF 0.4993, median 0.5205, 17 556 cells) — quote them from there.

### 2.5 If no name is eligible below the floor

The band is exhausted for that snapshot: record the snapshot id, the fetch time,
the page coverage, the market-cap floor and the exclusions in
`universe/last_scan.json`, keep `state = AWAITING_NEW_ELIGIBLE_CANDIDATES` and
set `next_eligible_refresh_at = scanned_at + 24 h`. That is a waiting state, not a
program stop (PROMPT.md §2.1.5): the ranking is refreshed again after 24 h and the
program continues when a new name appears below the floor.

**No section is written to `universe/mcap_expansion_log.md` in that case** — a
cycle that adds no name is not an expansion (that is the fix of 2026-10-22T06:55Z,
§5.2), and the next section of the log stays **Batch 27**.

**If the pass reports failed history probes** (`history_probe_failure_count > 0`,
state `INCOMPLETE_SCAN`): the eligibility of those names is *unknown*, not
negative. The band cannot be called exhausted on that pass. An early re-pass is
allowed for exactly this reason:
`refresh_universe.py fetch --override-gate --override-reason "history probes failed on the previous pass"`.

### 2.6 If the band still holds eligible names after the batch

A 20-page pass reaches far below the floor, so more than ten eligible names can
sit in the band. The remainder can be added **from the same frozen snapshot**,
without a new provider pass and without moving the 24 h bound (the bound belongs
to the ranking pass, not to the application):

```
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```

Do this only if the session has the time for it: each name costs ~2.5 min of
fixture download and ~1.7 min of grid. The names must be strictly below the
*current* floor, so the order is preserved. The second batch gets its own log
section (Batch 28) — the expansion key carries the names, not only the snapshot.

---

## 3. Acceptance checklist for the session that runs the expansion

* [ ] Exactly one ranking pass; the snapshot file is committed and linked from `universe/last_scan.json`.
* [ ] The pass covered **20 pages** and the snapshot records `pages_fetched == pages_requested` (a truncated pass is `INCOMPLETE_SCAN`, not an exhausted band).
* [ ] `universe/mcap_rank.json` grew by exactly the batch, in descending market-cap order, with the old 266 symbols untouched and in place.
* [ ] A fixture exists for every new symbol, with ≥ 17 520 hourly bars and a contiguous hourly grid, and `data/fixtures/fetch_manifest.json` has a provenance row for it.
* [ ] The grid holds 66 cells per new symbol: `results/20261019_135940_grid/progress.json` shows `completed_cells = (266 + n) × 66`, `next_cell = null`, 0 blocked.
* [ ] The fixtures of the 266 existing symbols were **not** re-fetched (their row counts and spans in `fetch_manifest.json` are unchanged) and `universe/last_scan.json` has no `fixture_conflicts`.
* [ ] `universe/last_scan.json` reports the new `universe_n`, the new floor, the remaining eligible count and `next_eligible_refresh_at = scanned_at + 24 h`.
* [ ] `universe/mcap_expansion_log.md` records previous N → new N, the rank range added and the ranking source/date — **once**, as `## Batch 27` (and `## Batch 28` for a second batch from the same snapshot). If the cycle added no name, the log is unchanged.
* [ ] `PYTHONPATH=. python3 -m pytest tests/ -q` passes (249 at the time of writing).

---

## 4. What must not happen

* No provider call before 2026-10-22T11:41:20Z, and no second pass inside the 24 h window afterwards.
* No re-run of the baseline grid, no re-opening of the child grid, no second worker on any run directory, no promotion from the child grid.
* No re-fetch of a fixture the grid already ran (it invalidates the stored cells). A missing fixture of a gridded symbol is a conflict to restore, not a download to repeat.
* No change to the registered grid, the cost model, the fill rule, the folds or the §3.4 gates.
* Operational: the `background_process` **monitor** action *starts* the command it is given
  instead of following it. A second copy of the verification run was started by mistake in
  the 2026-10-22 session and stopped within seconds; the check is read-only with respect
  to the grid, so nothing was affected. Use `start` + `logs`/`status` to follow a running
  process, and never two writers on one run directory.

---

## 5. Defects found and fixed in the expansion path

Five defects, all found by reading the code against the artifacts; none of them
changes the registered strategy, the cost model, the grid or the universe. The
first three were fixed on 2026-10-22T06:12Z, the last two on 2026-10-22T06:55Z.

### 5.1 The state could call an unobserved band exhausted (2026-10-22T06:12Z)

`phase_state` decided "the band below the floor is exhausted" from
`coverage_reaches_below_floor`, the flag the **ranking pass** wrote against the
floor it started from. A batch **lowers** the floor of the universe (the names
between the pass floor and the new floor are exactly the ones the batch
consumed), so a pass that stopped at the old floor never saw the band below the
new one. The record then said `AWAITING_NEW_ELIGIBLE_CANDIDATES` — the band is
exhausted, the program may wait 24 h — while the same record carried
`coverage_reaches_below_current_floor: false` and the phase printed the opposite
in its diagnostics. The exhausted state now requires the pass to have reached
below the **current** floor as well; otherwise the state is `INCOMPLETE_SCAN`
(PROMPT.md §2.1.5: an empty-but-complete ranking is not an incomplete scan, and
the other way round).

Consequence for the session that runs the expansion: **the state after the batch
is expected to be `EXPANSION_AVAILABLE`**, not `AWAITING_NEW_ELIGIBLE_CANDIDATES`.
A 20-page pass reaches far below the new floor, so the band below it is observed
and the eligible names in it are listed in `eligible_unseen_below_floor` — take
them from the same frozen snapshot (§2.6) instead of waiting 24 h. Only when the
record says `AWAITING_NEW_ELIGIBLE_CANDIDATES` (or `INCOMPLETE_SCAN` **with**
`coverage_reaches_below_current_floor: true`) is the band really exhausted.

### 5.2 The expansion log could be written twice (2026-10-22T06:12Z) — and could log the wrong batch (2026-10-22T06:55Z)

`phase_log` appended unconditionally, so a session that died after the `log`
phase and re-ran it produced two sections for one batch, and the generated
heading did not continue the `## Batch N` sequence. The phase is now idempotent
(each section carries `<!-- expansion-key: <snapshot_id>|<names> -->`) and
numbers its section `## Batch <next N> (applied <pass time>) - <names>
(N old -> new)`.

The second defect of the same phase: the names it logged came from the ranking
file's `added_in_this_expansion`, which names the **last expansion**, not the
current cycle. A ranking pass that finds no eligible name leaves that field
untouched, so the first `log` run of such a cycle appended a **second section
for batch 26** and consumed the number 27 that the next real expansion needs.
The phase now takes the names of the current cycle from the scan record
(`batch_selected`) and writes **nothing** when the cycle added no name.

### 5.3 The fixtures phase could re-fetch a symbol the grid already ran (2026-10-22T06:12Z)

The phase selected the ranking symbols whose fixture **file** was missing. A
symbol whose file is gone but whose 66 grid cells exist was therefore downloaded
again — which moves the bar sequence and makes all 66 stored cells stale. Such a
symbol is now skipped and reported as a conflict (`fixture_conflicts` in
`universe/last_scan.json`); the file has to be restored from the repository (the
fixtures are tracked in git) or the symbol re-gridded. It is never dropped from
the universe.

### 5.4 The state phase destroyed the expansion floor (2026-10-22T06:55Z)

The scan record stores the path of the frozen snapshot **relative to the
repository root**, and the phases resolved it against the working directory of
the session. A phase that was not run from the repository root therefore read
**no snapshot at all**, and the state phase computed the floor from an empty
ranking: `expansion_floor` became `{"symbol": null, "market_cap_usd": 0}`, the
state flipped to `INCOMPLETE_SCAN`, and a floor of $0 would have turned every
name of the ranking into a candidate below the floor. The snapshot path is now
resolved against the repository root (`scripts/refresh_universe.py:snapshot_of`),
and when the snapshot cannot be read at all the phase keeps the recorded floor
and says so instead of overwriting it.

### 5.5 The `fixtures` phase ran without the snapshot (2026-10-22T06:55Z)

Same root cause as §5.4, same fix: run from another working directory the
`fixtures` phase could not resolve the ranked price of a candidate, so the
price-identity check of the integrity gate silently became a no-op for every new
name (a fixture of a different asset would have been accepted). The snapshot is
read through the same `snapshot_of` helper now.

Tests: `249 passed` (244 + 5 new in `tests/test_refresh_universe.py`).

---

## 6. Useful facts about the current universe

* The band below the floor was **ten names wide** with 10 pages (the pass stopped at
  $15 931 465 against a floor of $16 279 472) and all ten are excluded: 4 without
  two years of hourly history (ELSA, MIRA, TUT, US) and 6 without a tradable KuCoin
  spot USDT pair (USDM, PIPPIN, M87, ARARA, STKRI, DRB). The exclusions were probed
  directly against the KuCoin candles API on 2026-10-21T11:44Z, so they are genuine
  and not transient API errors. **That narrow band is why the pass now covers 20
  pages**: the selection needs a supply of candidates below the floor, and a band
  of ten names that are all ineligible is no supply at all.
* A failed hourly-history probe is **unknown, not negative**
  (`scripts/fetch_mcap_snapshot.py:has_min_history` answers `True` / `False` /
  `None`). A name with a failed probe stays a candidate, the fixture download is
  the authoritative gate, and such a pass is recorded as `INCOMPLETE_SCAN`.
* Six included symbols have an ambiguous ticker in the ranking (SAFE, VELO, MEME,
  MASK, ONE, XAI). `scripts/fetch_mcap_snapshot.py` resolves those against the
  fixture the universe holds (the fix of 2026-10-22T05:05Z); the recorded floor
  is unaffected.
* `data/fixtures/` holds 268 CSV files: the 266 symbols of the universe, plus
  `CCD_USDT.csv` and `sample_hourly.csv`, which are not part of it. All 266
  fixtures of the universe are contiguous on the hourly grid (0 non-hourly steps)
  and carry 17 585 – 25 000 bars, so the integrity rule the `fixtures` phase
  applies to a new name is the rule the existing universe already satisfies
  (`scripts/validate_fixtures.py --all`: 268 checked, 0 invalid).
* The baseline grid was re-verified against the fixtures on
  2026-10-22T05:18Z (`results/20261022_052000_baseline_grid_repro`): 300 sampled
  cells reproduce their stored summary exactly, 0 stale. No fixture of an
  existing symbol has drifted, so the expansion only adds cells.
* A fixture whose hourly series has a gap (or fewer than 17 520 bars) is
  rejected by the `fixtures` phase and the name is removed from the ranking again
  and documented in the expansion log. That is deliberate: a partially gridded
  symbol would leave the grid permanently incomplete. The name is not "proven
  ineligible" — it can be re-examined in a later cycle.
* The 24 h bound is now held in one place, `scripts/refresh_gate.py`, and enforced
  by **both** tools that can query the provider: a record without a bound used to
  mean "the gate is open", and the classic path used to write exactly such a
  record whenever the band still held names (fixed 2026-10-22T06:05Z).

---

## 7. The closed mutation (context only — do not re-open it)

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
own null as the yardstick, not the parent's. Run it **after** the expansion, so
the child is a child of the expanded baseline.
