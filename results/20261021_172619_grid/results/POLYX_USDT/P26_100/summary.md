# EMA Hourly Continuation — POLYX/USDT P26_100

**Symbol:** POLYX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.6213 |
| sortino_ratio | -0.5253 |
| max_drawdown | 0.4970 |
| cagr | -0.2156 |
| net_avg_win | 77.2595 |
| net_avg_loss | -98.9223 |
| avg_hold_time_bars | 14.5734 |
| exposure | 0.3385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
