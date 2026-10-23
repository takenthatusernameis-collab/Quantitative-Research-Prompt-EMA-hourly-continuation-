# EMA Hourly Continuation — ALPINE/USDT P20_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8615 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.2141 |
| sortino_ratio | -0.8909 |
| max_drawdown | 0.6661 |
| cagr | -0.3409 |
| net_avg_win | 53.8994 |
| net_avg_loss | -75.8220 |
| avg_hold_time_bars | 37.8104 |
| exposure | 0.6617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
