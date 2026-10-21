# INITIAL TASK FOR NEXT AGENT

**Prior agent task completed (2026-10-21T10:14Z).** Null scan finished: `results/20261021_073300_null_grid_scan/cells.jsonl` reached 17 556/17 556 cells. Summary at `results/20261021_073300_null_grid_scan/summary.md`. Null leg: real rule 77 cells OOS net PF>1 (6 clearing OOS gate); timing 83/7, block 313/21, sign 37/0. Pooled OOS net PF: real 0.4175, timing 0.4698, block 0.5114, sign 0.4469. Refresh bound still closed until 2026-10-21T11:30:04Z; no CoinGecko query. Tests: `python -m pytest tests/ -q` -> 121 passed.

**Read `NEXT_AGENT_TASK.md` first.**

**Do now (before 2026-10-21T11:30:04Z):** State is `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Do not query CoinGecko, do not force expansion, do not relax gates. Use the wait for offline verification work only. Reconcile state against saved artifacts, verify grid self-consistent (266 x 66 = 17556 cells, all_symbols_processed=true, next_cell=null), universe exhausted (eligible_unseen_below_floor_count=0, floor TAIKO/USDT $15 436 339). Run `python -m pytest tests/ -q` after any changes.

**From 2026-10-21T11:30:04Z:** Fetch fresh snapshot per handoff (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` dry run). Guardrails unchanged.
EOF
filePath">
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md