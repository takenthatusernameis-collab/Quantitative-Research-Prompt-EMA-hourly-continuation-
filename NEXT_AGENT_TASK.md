# NEXT AGENT TASK

## Current state (verified, 2026-10-20)

**Program status: `EXPANSION_AVAILABLE`.** Batch 19 (universe N 187 -> 197) is **complete**: 10 new symbols (OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI) each have 66 EMA cells -> 13 002 / 13 002 cells, 0 blocked. Aggregate re-run: mean net PF 0.4959, median 0.5162, best 2.2274; 36 cells net PF > 1, all rejected by OOS + 2x cost -> 0 credible candidates. Tests: 56 passed.

- Universe: N = 197, floor CATI/USDT USD 33 051 490.
- Grid: 13 002 / 13 002 cells in `results/20261019_135940_grid/`.
- Candidate check artifact: latest run under `results/20261020_*_candidate_check/` (0 credible).

## Required next action

Apply next 10 eligible names from saved snapshot `universe/mcap_snapshot_20261020_113004.json` (METIS, REZ, LISTA, COTI, MAGIC, GTC, MANTA, LUNA, FLUX, XCH) using the apply script, fetch fixtures, run 66-pair grid ranks 198-207, re-run aggregate + candidate check, update log/handoff. Do not re-run completed cells.

## Guardrails

Append-only market-cap order; no in-sample promotion; run tests after code changes.