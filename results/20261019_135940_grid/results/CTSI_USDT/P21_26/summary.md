# EMA Hourly Continuation — CTSI/USDT P21_26

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.2360 |
| net_win_rate | 0.3691 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -13.5167 |
| sortino_ratio | -6.7221 |
| max_drawdown | 0.9998 |
| cagr | -0.9694 |
| net_avg_win | 7.0662 |
| net_avg_loss | -17.5186 |
| avg_hold_time_bars | 2.7314 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
