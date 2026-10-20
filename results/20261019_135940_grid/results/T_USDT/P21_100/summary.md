# EMA Hourly Continuation — T/USDT P21_100

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6246 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -3.9914 |
| sortino_ratio | -1.3533 |
| max_drawdown | 0.8088 |
| cagr | -0.4773 |
| net_avg_win | 48.1908 |
| net_avg_loss | -70.3294 |
| avg_hold_time_bars | 15.1870 |
| exposure | 0.4007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
