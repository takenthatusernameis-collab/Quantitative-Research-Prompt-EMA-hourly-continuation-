# EMA Hourly Continuation — AEVO/USDT P34_200

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8561 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1296 |
| gross_win_rate | 0.5327 |
| sharpe_ratio | -0.8215 |
| sortino_ratio | -0.2159 |
| max_drawdown | 0.2578 |
| cagr | -0.0967 |
| net_avg_win | 75.6849 |
| net_avg_loss | -99.5927 |
| avg_hold_time_bars | 36.4881 |
| exposure | 0.5548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
