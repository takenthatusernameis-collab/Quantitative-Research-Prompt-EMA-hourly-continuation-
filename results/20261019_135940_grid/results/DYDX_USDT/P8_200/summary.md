# EMA Hourly Continuation — DYDX/USDT P8_200

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.2912 |
| sortino_ratio | -0.5385 |
| max_drawdown | 0.5013 |
| cagr | -0.2306 |
| net_avg_win | 64.3635 |
| net_avg_loss | -90.6838 |
| avg_hold_time_bars | 65.3169 |
| exposure | 0.8432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
