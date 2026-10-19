# NEXT AGENT TASK

## Objective
**Active.** Run the **full EMA period combination grid** on hourly continuation for each symbol in **market-cap descending** order, and **keep expanding** to lower market-cap candidates even if prior symbols/pairs failed to find an edge.

Authoritative rules: `PROMPT.md` (updated 2026-10-19). User-authorized program change supersedes the prior “stand down after 50/100 rejection” handoff.

## Prior result (immutable, do not overwrite)
- EMA **50/100** on top-5 (BTC/ETH/SOL/BNB/XRP) was **rejected** OOS net-of-costs: 666 trades, net PF 0.6890, net Sharpe −1.9443 (`results/FINAL_DECISION.md`, `results/20261019_064215_oos_pooled/`).
- Keep those artifacts as historical evidence for the single pair `(50, 100)`. They do **not** cancel the full grid or expansion.

## Current mandate
1. Parameterize `P_fast` / `P_slow` from the registered period set in `PROMPT.md` §1.1: `{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}` with `P_fast < P_slow`.
2. For **each** eligible symbol (mcap descending): run **all** valid pairs—not only 50/100.
3. Persist one result set per `(symbol, P_fast, P_slow)`.
4. When the current snapshot’s candidates are fully processed (grid complete or skipped with reason), **expand** to the next lower market-cap batch (`PROMPT.md` §2.1) and repeat the full grid.
5. **Continue after total failure:** if every prior candidate and every pair is rejected, still expand and test new descending-mcap names.

## Acceptance for this session
- Implement or wire a grid runner (or document the exact next command) that iterates symbols × EMA pairs.
- Produce or extend artifacts under `results/` with configs that record `P_fast`, `P_slow`, symbol.
- Leave a handoff naming the next unprocessed symbol/pair or next expansion batch.
- Tests: `python -m pytest tests/ -q` (extend tests for parameterized periods if you change signal code).

## Constraints
- Do not claim live edge without OOS net-of-costs + robustness.
- Do not fabricate data.
- Do not delete or rewrite the historical 50/100 rejection artifacts; add new cells beside them.
- Multiple-testing: report the full grid honestly; do not promote a single lucky cell without OOS and cost stress.

## Validation Command
`python -m pytest tests/ -q`
