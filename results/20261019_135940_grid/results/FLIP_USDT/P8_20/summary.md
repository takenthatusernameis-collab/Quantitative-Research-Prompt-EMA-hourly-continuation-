# EMA Hourly Continuation — FLIP/USDT P8_20

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.3265 |
| net_win_rate | 0.3561 |
| gross_profit_factor | 0.7623 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -13.0009 |
| sortino_ratio | -6.3343 |
| max_drawdown | 0.9998 |
| cagr | -0.9642 |
| net_avg_win | 11.7612 |
| net_avg_loss | -19.9239 |
| avg_hold_time_bars | 5.6897 |
| exposure | 0.2992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
