# EMA Hourly Continuation — RIO/USDT P21_26

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1282 |
| net_profit_factor | 0.2411 |
| net_win_rate | 0.3167 |
| gross_profit_factor | 0.5344 |
| gross_win_rate | 0.3339 |
| sharpe_ratio | -15.0378 |
| sortino_ratio | -7.7630 |
| max_drawdown | 1.0000 |
| cagr | -0.9831 |
| net_avg_win | 7.8234 |
| net_avg_loss | -15.0410 |
| avg_hold_time_bars | 2.0507 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
