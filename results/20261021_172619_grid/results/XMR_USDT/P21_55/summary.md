# EMA Hourly Continuation — XMR/USDT P21_55

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6594 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9122 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.8293 |
| sortino_ratio | -0.8464 |
| max_drawdown | 0.6282 |
| cagr | -0.3207 |
| net_avg_win | 58.1124 |
| net_avg_loss | -78.6349 |
| avg_hold_time_bars | 6.7449 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
