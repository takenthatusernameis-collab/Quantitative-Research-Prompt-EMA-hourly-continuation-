# EMA Hourly Continuation — SHR/USDT P21_26

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1383 |
| net_profit_factor | 0.1971 |
| net_win_rate | 0.2480 |
| gross_profit_factor | 0.4271 |
| gross_win_rate | 0.2617 |
| sharpe_ratio | -18.1549 |
| sortino_ratio | -9.7414 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 7.1574 |
| net_avg_loss | -11.9759 |
| avg_hold_time_bars | 2.1750 |
| exposure | 0.1361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
