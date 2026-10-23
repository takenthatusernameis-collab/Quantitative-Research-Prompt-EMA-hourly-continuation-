# EMA Hourly Continuation — ONT/USDT P21_50

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.5111 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.9257 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -7.8563 |
| sortino_ratio | -3.4261 |
| max_drawdown | 0.9861 |
| cagr | -0.8128 |
| net_avg_win | 25.2438 |
| net_avg_loss | -36.9110 |
| avg_hold_time_bars | 4.6845 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
