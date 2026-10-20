# EMA Hourly Continuation — BOME/USDT P8_21

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1616 |
| net_profit_factor | 0.4665 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8515 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -9.2652 |
| sortino_ratio | -5.2169 |
| max_drawdown | 0.9985 |
| cagr | -0.9251 |
| net_avg_win | 11.9598 |
| net_avg_loss | -21.1238 |
| avg_hold_time_bars | 2.9468 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
