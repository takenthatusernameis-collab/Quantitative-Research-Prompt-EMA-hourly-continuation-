# EMA Hourly Continuation — RPL/USDT P21_100

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7770 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.8714 |
| sortino_ratio | -0.5943 |
| max_drawdown | 0.5186 |
| cagr | -0.2399 |
| net_avg_win | 71.8794 |
| net_avg_loss | -87.7955 |
| avg_hold_time_bars | 19.2113 |
| exposure | 0.4321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
