# EMA Hourly Continuation — DODO/USDT P21_55

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5418 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.9176 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -7.8361 |
| sortino_ratio | -3.4892 |
| max_drawdown | 0.9877 |
| cagr | -0.8215 |
| net_avg_win | 26.8883 |
| net_avg_loss | -37.2667 |
| avg_hold_time_bars | 5.5346 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
