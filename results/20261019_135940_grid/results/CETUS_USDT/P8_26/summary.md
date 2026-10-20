# EMA Hourly Continuation — CETUS/USDT P8_26

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1524 |
| net_profit_factor | 0.5070 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -9.2371 |
| sortino_ratio | -5.0250 |
| max_drawdown | 0.9982 |
| cagr | -0.9180 |
| net_avg_win | 15.3666 |
| net_avg_loss | -23.6527 |
| avg_hold_time_bars | 3.9016 |
| exposure | 0.2691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
