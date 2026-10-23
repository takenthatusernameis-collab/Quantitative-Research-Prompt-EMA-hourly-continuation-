# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

## Update 2026-10-23T19:33 UTC (this session, re-check)

Prior agent task (read from durable handoff) completed as offline-only verification:
`PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → `{'eligible': False, 'bound': '2026-10-24T12:28:28.949476+00:00', 'now': '2026-10-23T19:33:06.680607+00:00', 'reason': 'the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not elapsed yet'}`. No provider contact made — the bound has not elapsed.

State re-verified from disk, not from memory:
- `universe/last_scan.json`: `state = AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n = 275`, `snapshot_id = mcap_snapshot_20261023_122828`, `scanned_at = 2026-10-23T12:28:28.949476+00:00`, coverage 20 pages / 2 000 entries / lowest $3 441 774, `expansion_floor = BOSON/USDT $3 558 643`, `eligible_unseen_below_floor_count = 0`, `batch_selected = []`, `next_eligible_refresh_at = 2026-10-24T12:28:28.949476+00:00`.
- Baseline grid `results/20261019_135940_grid`: complete, 18 150/18 150 cells, 0 blocked, `all_symbols_processed = true`, `next_cell = null`. Pooled mean net PF 0.4987, median 0.5198, 37 cells net PF > 1 (0.20 % vs ~50 % null), 27 exploratory, 18 123 rejected, **0 credible candidates**.
- `results/mutations.json`: `C_stricter_trend` and `C_min_risk_atr` both **NOT_PROMOTED**. Baseline grid remains the program grid.
- Null grid scan `results/20261023_050716_null_grid_scan/`: no edge.

**Your job:** wait until 2026-10-24T12:28:28.949476Z, then execute the refresh cycle. Do not contact CoinGecko or KuCoin before that timestamp.

## Your task (in order)

1. Verify eligibility offline first: `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must return `eligible: True`.
2. Run exactly one 20-page market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20` (or `scripts/refresh_universe.py fetch`).
3. Freeze the new snapshot for 24 h.
4. Re-check the band below the then-current floor for eligible unseen candidates.
5. If candidates exist, expand per PROMPT.md §2.1 (append next lower market-cap candidates descending, log to `universe/mcap_expansion_log.md`, fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`).
6. If no candidates exist, record the pass and set state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES` (next bound +24 h).
7. Update `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the next bound and next unprocessed symbol/pair batch.

## Constraints

- No provider call before 2026-10-24T12:28:28.949476Z.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`) in any run.
- Do not stop the program because prior pairs/symbols failed — expand descending market cap and continue (PROMPT.md §2.1.4, §6.7).
