# EMA Hourly Continuation — AXL/USDT P21_50

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1063 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -7.8632 |
| sortino_ratio | -3.6014 |
| max_drawdown | 0.9879 |
| cagr | -0.8251 |
| net_avg_win | 25.3794 |
| net_avg_loss | -34.8418 |
| avg_hold_time_bars | 4.4619 |
| exposure | 0.2146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
