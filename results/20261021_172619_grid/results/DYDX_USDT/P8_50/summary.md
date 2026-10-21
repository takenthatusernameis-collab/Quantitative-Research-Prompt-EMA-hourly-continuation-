# EMA Hourly Continuation — DYDX/USDT P8_50

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.7499 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.1998 |
| sortino_ratio | -0.8150 |
| max_drawdown | 0.6255 |
| cagr | -0.3129 |
| net_avg_win | 55.6145 |
| net_avg_loss | -70.9318 |
| avg_hold_time_bars | 14.9019 |
| exposure | 0.4559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
