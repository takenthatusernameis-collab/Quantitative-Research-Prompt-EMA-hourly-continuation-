# INITIAL TASK FOR NEXT AGENT

Batch 12 partial: universe N=127 declared (mcap_rank.json updated) but only 4 of 10 new names (DYDX, MINA, ZRX, WEMIX) had KuCoin fixtures and were grid-processed (N=117 -> 121, 7,986 cells). GMX, PROM, W, ARKM, LPT, SAFE are unsupported on KuCoin (HTTP 400100). Cumulative: 7,983 rejected / 7,986 cells, 3 exploratory (JASMY P20_200, JASMY P21_200, SUPER P8_200), 0 credible candidates. Tests 46 passed.

NEXT: resolve the 6 unsupported symbols - find an alternate source (Binance/Bybit/OKX) or drop them from universe per PROMPT.md §2.1.2 (append-only; dropping requires documented justification). Then fetch OHLCV, run grid --n 122..127 (or adjusted), aggregate, candidate_check, update handoff.

Environment: pip install pandas numpy pytest first. Use PYTHONPATH=. python3.
