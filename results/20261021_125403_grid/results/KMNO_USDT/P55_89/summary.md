# EMA Hourly Continuation — KMNO/USDT P55_89

**Symbol:** KMNO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7973 |
| net_win_rate | 0.5204 |
| gross_profit_factor | 1.0650 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -1.1374 |
| sortino_ratio | -0.2826 |
| max_drawdown | 0.2901 |
| cagr | -0.1226 |
| net_avg_win | 70.9897 |
| net_avg_loss | -96.6204 |
| avg_hold_time_bars | 8.2789 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
