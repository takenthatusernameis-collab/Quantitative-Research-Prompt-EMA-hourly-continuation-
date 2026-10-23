# NEXT TASK — stricter-trend mutation complete (NOT_PROMOTED); null scan running; universe refresh pending (updated 2026-10-23T06:15:43Z)

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
| Null grid scan | **running** — `results/20261023_050716_null_grid_scan`, ~3 696 / 18 150 cells checkpointed (~1 cell/s, 4 workers), bgp `bgp_16727f875001PN9OCuMW630ors` |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify state offline and stop cleanly. The expansion belongs to the first session that runs after the bound.

---

## 2. Completed work — stricter-trend single-variable mutation (offline)

Decision: NOT_PROMOTED. Recorded in `results/mutations.json` child `C_stricter_trend` (`status = complete`). The `stricter_trend` flag is a no-op. No edge, no promotion; baseline grid stays the program grid.

---

## 3. Next task — universe refresh (after 2026-10-23T12:15:58Z)

The next step belongs to the first session that runs **after** 2026-10-23T12:15:58Z:

1. Verify `background_process status bgp_16727f875001PN9OCuMW630ors` (null grid scan) has completed; if not, wait for it. On exit, run `PYTHONPATH=. python3 scripts/null_grid_scan.py --summarize-only results/20261023_050716_null_grid_scan` to produce `summary.json` / `summary.md`.
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
