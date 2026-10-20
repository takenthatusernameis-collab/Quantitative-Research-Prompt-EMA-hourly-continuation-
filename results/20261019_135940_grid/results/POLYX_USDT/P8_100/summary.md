# EMA Hourly Continuation — POLYX/USDT P8_100

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.7286 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0456 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -2.8033 |
| sortino_ratio | -0.9900 |
| max_drawdown | 0.7350 |
| cagr | -0.3756 |
| net_avg_win | 59.8578 |
| net_avg_loss | -80.6047 |
| avg_hold_time_bars | 23.2054 |
| exposure | 0.6624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
