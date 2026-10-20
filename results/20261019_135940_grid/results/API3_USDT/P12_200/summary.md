# EMA Hourly Continuation — API3/USDT P12_200

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7453 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.9840 |
| sortino_ratio | -0.5678 |
| max_drawdown | 0.5356 |
| cagr | -0.2369 |
| net_avg_win | 70.6853 |
| net_avg_loss | -92.5752 |
| avg_hold_time_bars | 38.9492 |
| exposure | 0.7312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
