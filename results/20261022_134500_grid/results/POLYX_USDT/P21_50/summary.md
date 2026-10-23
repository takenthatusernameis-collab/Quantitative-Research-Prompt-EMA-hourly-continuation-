# EMA Hourly Continuation — POLYX/USDT P21_50

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.5293 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -6.5500 |
| sortino_ratio | -2.7902 |
| max_drawdown | 0.9682 |
| cagr | -0.7426 |
| net_avg_win | 25.7673 |
| net_avg_loss | -41.5842 |
| avg_hold_time_bars | 5.2445 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
