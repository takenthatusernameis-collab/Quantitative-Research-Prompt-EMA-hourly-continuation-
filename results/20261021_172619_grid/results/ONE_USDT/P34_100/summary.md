# EMA Hourly Continuation — ONE/USDT P34_100

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.9180 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1266 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -0.5674 |
| sortino_ratio | -0.1701 |
| max_drawdown | 0.3422 |
| cagr | -0.0795 |
| net_avg_win | 92.1840 |
| net_avg_loss | -112.7873 |
| avg_hold_time_bars | 13.0116 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
