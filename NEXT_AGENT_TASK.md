# NEXT AGENT TASK

## Objective
**Active / In progress.** Run the **full EMA period combination grid** on hourly continuation for each symbol in **market-cap descending** order, and **keep expanding** to lower market-cap candidates even if prior symbols/pairs failed to find an edge.

Authoritative rules: `PROMPT.md` (updated 2026-10-19). User-authorized program change supersedes the prior "stand down after 50/100 rejection" handoff. `RESEARCH_CONCLUSION.md` / `FINAL_DECISION.md` describe the rejected 50/100 baseline only; they do **not** cancel the grid or expansion.

## Prior result (immutable, do not overwrite)
- EMA **50/100** on top-5 (BTC/ETH/SOL/BNB/XRP) was **rejected** OOS net-of-costs: 666 trades, net PF 0.6890, net Sharpe −1.9443 (`results/FINAL_DECISION.md`, `results/20261019_064215_oos_pooled/`).
- Keep those artifacts as historical evidence for the single pair `(50, 100)`. They do **not** cancel the full grid or expansion.

## Progress this session (2026-10-19)
- Parameterized `signals/signals.py`: `generate_signals(df, ema_fast_period=50, ema_slow_period=100)` now writes `ema_fast`/`ema_slow` columns; backtest reads `ema_slow` for SL/TP risk (`P_fast < P_slow` enforced).
- `backtest/backtest.py` uses `ema_slow` column (with `ema100` fallback) for risk = |entry − EMA_slow[t]|.
- Created `scripts/run_grid.py`: iterates symbols × all valid `(P_fast, P_slow)` pairs from `PERIOD_GRID = {8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}` and persists one artifact set per cell under `results/<RUNID>_grid/results/<SYMBOL>/P{fast}_{slow}/` (config.json, trades.csv, equity.csv, summary.json, summary.md) plus `run_config.json` and `progress.json` (resume-safe).
- **BTC/USDT full grid complete: 66/66 cells**, all net PF < 1 (rejected). Artifacts: `results/20261019_125056_grid/`.
- Tests extended for parameterized periods; `python -m pytest tests/ -q` → **17/17 pass**.

## Current mandate
1. Period set (PROMPT.md §1.1): `{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}` with `P_fast < P_slow` (66 pairs).
2. For **each** eligible symbol (mcap descending): run **all** valid pairs — not only 50/100.
3. Persist one result set per `(symbol, P_fast, P_slow)` (config records `P_fast`, `P_slow`, symbol, costs, fill rule).
4. **Next unprocessed cell: `ETH/USDT P8_12`**, then remaining ETH pairs, then `SOL/USDT`, `BNB/USDT`, `XRP/USDT` (universe: `universe/mcap_rank.json` = [BTC, ETH, SOL, BNB, XRP]).
5. When current snapshot's candidates are fully processed, **expand** to the next lower market-cap batch (PROMPT.md §2.1) and repeat the full grid.
6. **Continue after total failure:** if every prior candidate and pair is rejected, still expand and test new descending-mcap names.

## Continue command (next cell)
```
PYTHONPATH=. python scripts/run_grid.py --n 5 --taker-fee-bps 10 --slippage-bps 2 --rr 1.0
```
(uses `universe/mcap_rank.json`; resumes automatically via `progress.json` if re-run on the same `results/<RUNID>_grid` dir with `--resume`).

## Acceptance for this session
- Grid runner implemented and wired: `scripts/run_grid.py` iterates symbols × EMA pairs.
- Artifacts under `results/` with configs recording `P_fast`, `P_slow`, symbol.
- Handoff names the next unprocessed symbol/pair: `ETH/USDT P8_12`.
- Tests: `python -m pytest tests/ -q` (17/17 pass).

## Handoff Notes
- Signals/backtest parameterized for arbitrary EMA periods (defaults 50/100 keep prior behavior).
- BTC/USDT 66 cells complete, all rejected (net PF < 1); artifacts at `results/20261019_125056_grid/`.
- Next agent starts at `ETH/USDT P8_12`.
- Tests: 17/17 pass (`python -m pytest tests/ -q`).

## Constraints
- Do not claim live edge without OOS net-of-costs + robustness.
- Do not fabricate data.
- Do not delete or rewrite the historical 50/100 rejection artifacts; add new cells beside them.
- Multiple-testing: report the full grid honestly; do not promote a single lucky cell without OOS and cost stress.

## Validation Command
`python -m pytest tests/ -q`
