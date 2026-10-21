# EMA Hourly Continuation — PROM/USDT P12_20

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.4953 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7980 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -4.9610 |
| sortino_ratio | -1.4634 |
| max_drawdown | 0.8217 |
| cagr | -0.4954 |
| net_avg_win | 45.2366 |
| net_avg_loss | -65.2888 |
| avg_hold_time_bars | 5.9040 |
| exposure | 0.1146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
