# EMA Hourly Continuation — BAND/USDT P8_12

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1581 |
| net_profit_factor | 0.1988 |
| net_win_rate | 0.3960 |
| gross_profit_factor | 0.6861 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -14.6224 |
| sortino_ratio | -8.2996 |
| max_drawdown | 1.0000 |
| cagr | -0.9874 |
| net_avg_win | 3.9624 |
| net_avg_loss | -13.0684 |
| avg_hold_time_bars | 2.4845 |
| exposure | 0.1777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
