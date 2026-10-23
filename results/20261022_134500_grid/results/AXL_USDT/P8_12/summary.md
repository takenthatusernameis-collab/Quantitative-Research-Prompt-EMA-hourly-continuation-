# EMA Hourly Continuation — AXL/USDT P8_12

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1878 |
| net_profit_factor | 0.2233 |
| net_win_rate | 0.3541 |
| gross_profit_factor | 0.6406 |
| gross_win_rate | 0.3887 |
| sharpe_ratio | -17.5631 |
| sortino_ratio | -10.8800 |
| max_drawdown | 1.0000 |
| cagr | -0.9968 |
| net_avg_win | 4.3244 |
| net_avg_loss | -10.6148 |
| avg_hold_time_bars | 2.0346 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
