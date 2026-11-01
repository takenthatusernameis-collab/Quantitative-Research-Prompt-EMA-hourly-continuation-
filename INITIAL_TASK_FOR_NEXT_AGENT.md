# Initial Task for Next Agent

Gate is NOT ELIGIBLE until bound `2026-11-01T23:24:44.567699+00:00` (~13.3h remaining). Do not query provider.

At/after bound:
1. Offline gate check first (`scripts/refresh_gate.gate_status` on `universe/last_scan.json`).
2. If eligible: run at most one 20-page pass: `scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor, inspect below-floor band, update `universe/last_scan.json`.
4. Do NOT apply pending batch (NIM/SUKU) this cycle (no fixtures/grid coverage).
5. No grid reruns, no candle fetches, no cost/fill changes. Keep strict confirmatory separate from exploratory.

Constraints: historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.
