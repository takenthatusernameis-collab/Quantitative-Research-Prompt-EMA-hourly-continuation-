# EMA Hourly Continuation — AAVE/USDT P12_200

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8197 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.0226 |
| sortino_ratio | -0.2484 |
| max_drawdown | 0.3108 |
| cagr | -0.1093 |
| net_avg_win | 80.1878 |
| net_avg_loss | -95.1674 |
| avg_hold_time_bars | 54.3138 |
| exposure | 0.7160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
