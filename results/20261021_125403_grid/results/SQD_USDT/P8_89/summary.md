# EMA Hourly Continuation — SQD/USDT P8_89

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.8272 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.3288 |
| sortino_ratio | -0.4564 |
| max_drawdown | 0.4245 |
| cagr | -0.1926 |
| net_avg_win | 70.2958 |
| net_avg_loss | -82.8737 |
| avg_hold_time_bars | 20.1395 |
| exposure | 0.5292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
