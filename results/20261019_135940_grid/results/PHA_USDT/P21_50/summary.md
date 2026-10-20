# EMA Hourly Continuation — PHA/USDT P21_50

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8451 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -6.8572 |
| sortino_ratio | -3.0536 |
| max_drawdown | 0.9765 |
| cagr | -0.7740 |
| net_avg_win | 21.3260 |
| net_avg_loss | -34.7883 |
| avg_hold_time_bars | 4.5640 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
