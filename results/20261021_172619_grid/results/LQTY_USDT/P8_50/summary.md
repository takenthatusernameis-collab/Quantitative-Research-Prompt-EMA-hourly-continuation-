# EMA Hourly Continuation — LQTY/USDT P8_50

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.7743 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.0993 |
| sortino_ratio | -0.7964 |
| max_drawdown | 0.6167 |
| cagr | -0.3072 |
| net_avg_win | 59.0163 |
| net_avg_loss | -75.3607 |
| avg_hold_time_bars | 15.4816 |
| exposure | 0.4946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
