# NEXT TASK — session active 08:32 UTC; null scan checkpointed ~56% (env lacks numpy/pandas); refresh bound 12:15:58Z (updated 2026-10-23T08:32:00Z)

Read this file first. It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `NULL_SCAN_BLOCKED` + refresh-bound waiting (this session) |
| Stricter-trend mutation | closed — `results/20261022_134500_grid`, `stricter_trend: true`, **NOT_PROMOTED** (zero-delta no-op) |
| ATR min-risk mutation | closed, **NOT_PROMOTED** |
| Baseline grid | `results/20261019_135940_grid` — complete, 0 blocked, remains the program grid |
| Universe | N = 275, floor `ALPINE/USDT` $3 614 141 |
| Frozen snapshot | `universe/mcap_snapshot_20261022_121558.json` (fetched 2026-10-22T12:15:58Z) |
| Next eligible universe refresh | **2026-10-23T12:15:58Z — no provider contact before then** |
| Null grid scan | **blocked in this env**: `results/20261023_050716_null_grid_scan`, **10 230 / 18 150 cells (~56 %)** checkpointed in `cells.jsonl`; resume requires numpy+pandas (not installed in `/usr/bin/python3`; the resume attempt failed with `ModuleNotFoundError: No module named 'numpy'`). Next step on resume: `--summarize-only` → `summary.json` / `summary.md` |
| Tests | `249 passed` claimed in prior handoff, **NOT verifiable here** (`pytest`, `numpy`, `pandas` not installed in `/usr/bin/python3`) |

**Provider discipline.** Until 2026-10-23T12:15:58Z the market-data provider must not be contacted at all. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 12:15:58Z must not fetch: verify state offline and stop cleanly. The expansion belongs to the first session that runs after the bound.

---

## 2. Completed work — mutations (offline, closed)

Decision: NOT_PROMOTED for both `C_stricter_trend` and `C_min_risk_atr`. Recorded in `results/mutations.json`. Neither produced an edge; baseline grid stays the program grid. See `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`.

---

## 3. Next task

1. **Null grid scan (offline, needs numpy+pandas):** resume `results/20261023_050716_null_grid_scan` (auto-resumes from the 10 230-cell checkpoint) in an environment with numpy+pandas:
   `PYTHONPATH=. python3 scripts/null_grid_scan.py --run results/20261022_134500_grid --workers 4 --out results/20261023_050716_null_grid_scan`
   then summarize:
   `PYTHONPATH=. python3 scripts/null_grid_scan.py --summarize-only results/20261023_050716_null_grid_scan`
   → `summary.json` / `summary.md`. Expected result matches baseline null (no edge).
2. **After 12:15:58Z:** run exactly one market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py` (or equivalent), then freeze the new snapshot for 24 h.
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
