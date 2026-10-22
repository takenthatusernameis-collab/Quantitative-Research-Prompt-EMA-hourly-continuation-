# EMA Hourly Continuation — POL/USDT P8_12

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1907 |
| net_profit_factor | 0.1625 |
| net_win_rate | 0.3125 |
| gross_profit_factor | 0.5968 |
| gross_win_rate | 0.3818 |
| sharpe_ratio | -21.1489 |
| sortino_ratio | -13.6154 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 3.2566 |
| net_avg_loss | -9.1082 |
| avg_hold_time_bars | 1.7514 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
