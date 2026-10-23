# NEXT TASK — stricter-trend mutation complete (NOT_PROMOTED); null scan running; universe refresh pending (updated 2026-10-23T05:52:00Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `MUTATION_COMPLETE` |
| Stricter-trend mutation | **closed** — `results/20261022_134500_grid`, `stricter_trend: true`, **NOT_PROMOTED** (zero-delta no-op) |
| Baseline grid | `results/20261019_135940_grid` — complete, 0 blocked, remains the program grid |
| Universe | N = 275, floor `ALPINE/USDT` $3 614 141 |
| Frozen snapshot | `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z) |
| Next eligible universe refresh | **2026-10-23T12:15:58Z — no provider contact before then** |
| ATR min-risk mutation | closed `NOT_PROMOTED` |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) |
| Null grid scan | **running** — `results/20261023_050716_null_grid_scan`, 2 310 / 18 150 cells checkpointed (~1 cell/s, 4 workers) |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify state offline and stop cleanly. The expansion belongs to the first session that runs after the bound.

---

## 2. Completed work — stricter-trend single-variable mutation (offline)

The expansion finished at 2026-10-22T13:20Z: N = 275, floor `ALPINE/USDT` $3 614 141, mean net PF 0.4987, 37 cells net PF > 1, candidate_check rejected all, tests 249 passed. The baseline grid `results/20261019_135940_grid` is the 275-symbol expanded baseline (18 150 cells).

One registered variable was flipped on the expanded baseline: `stricter_trend: true` (PROMPT.md §5.1 — entry also requires close above/below EMAslow). The ATR min-risk filter stays closed (`NOT_PROMOTED`). Registered costs, rr 1.0, conservative exit, risk sizing, folds, entry/exit semantics and §3.4 gates are unchanged.

### Results

All evaluation legs ran against child `results/20261022_134500_grid` vs parent `results/20261019_135940_grid` (18 150 cells each):

| Leg | Result |
|---|---|
| `aggregate_grid.py` | mean net PF 0.4987, 37 cells PF > 1, 0 blocked |
| `candidate_check.py` | all 37 cells rejected; 0 promoted |
| `mutation_eval.py` | **zero delta on every metric** — pooled net PF 0.5219 identical, OOS net PF 0.5282 identical, walk-forward OOF net PF 0.6404 identical, trades 14676563 identical |
| `mutation_repro_check.py` | 16/16 child and parent cells reproduce exactly; 0 entry-bar divergence |
| `mutation_survivor_check.py` | 10 cells clear §3.4 gate (same as baseline), 1 of 10 sub-period stable |
| `null_grid_scan.py` | running as background process `bgp_16727f875001PN9OCuMW630ors` (confirmatory; zero-delta grid means result matches baseline null) |
| `pytest tests/ -q` | 249 passed |

**Decision: NOT_PROMOTED.** Recorded in `results/mutations.json` child `C_stricter_trend` (`status = complete`). The `stricter_trend` flag is a no-op: the entry cross (close crosses EMAfast in the direction of `EMAfast > EMAslow`) already implies close above/below EMAslow, so flipping the flag changes nothing. No edge, no promotion; baseline grid stays the program grid.

---

## 3. Next task — universe refresh (after 2026-10-23T12:15:58Z)

The next step belongs to the first session that runs **after** 2026-10-23T12:15:58Z:

1. Verify `background_process status bgp_16727f875001PN9OCuMW630ors` (null grid scan) has completed; if not, wait for it.
2. After 12:15:58Z, run exactly one market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py` (or equivalent), then freeze the new snapshot for 24 h.
3. Expand the universe per PROMPT.md §2.1 (append next lower market-cap candidates, descending order) and run the full EMA grid on new symbols.
4. Update `universe/mcap_expansion_log.md`, `NEXT_AGENT_TASK.md`, and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

Until the refresh bound, no provider contact is permitted. Work on offline artifacts, diagnostics, or stop cleanly.

---

## 4. What must not happen

- No provider call before 2026-10-23T12:15:58Z.
- No second writer on `results/20261022_134500_grid`, no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`) in any run.

(End of file)