# EMA Hourly Continuation — NUM/USDT P8_12

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1598 |
| net_profit_factor | 0.1802 |
| net_win_rate | 0.2735 |
| gross_profit_factor | 0.7292 |
| gross_win_rate | 0.3329 |
| sharpe_ratio | -19.6942 |
| sortino_ratio | -11.5276 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 5.0310 |
| net_avg_loss | -10.5069 |
| avg_hold_time_bars | 2.5864 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
