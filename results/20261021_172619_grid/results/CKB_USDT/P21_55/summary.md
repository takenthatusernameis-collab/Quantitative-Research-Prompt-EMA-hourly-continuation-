# EMA Hourly Continuation — CKB/USDT P21_55

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.7074 |
| sortino_ratio | -0.8949 |
| max_drawdown | 0.6569 |
| cagr | -0.3362 |
| net_avg_win | 59.3122 |
| net_avg_loss | -78.4447 |
| avg_hold_time_bars | 7.7794 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
