# EMA Hourly Continuation — SQD/USDT P89_200

**Symbol:** SQD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7846 |
| net_win_rate | 0.5121 |
| gross_profit_factor | 1.0817 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -1.4818 |
| sortino_ratio | -0.4140 |
| max_drawdown | 0.4078 |
| cagr | -0.1755 |
| net_avg_win | 71.7482 |
| net_avg_loss | -95.9905 |
| avg_hold_time_bars | 10.8544 |
| exposure | 0.1893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
