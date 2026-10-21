# EMA Hourly Continuation — NMR/USDT P20_50

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.7001 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9584 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.2483 |
| sortino_ratio | -1.1360 |
| max_drawdown | 0.7442 |
| cagr | -0.4063 |
| net_avg_win | 59.3901 |
| net_avg_loss | -77.7812 |
| avg_hold_time_bars | 7.2667 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
