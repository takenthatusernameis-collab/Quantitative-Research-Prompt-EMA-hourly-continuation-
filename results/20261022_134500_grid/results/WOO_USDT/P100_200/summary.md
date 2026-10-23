# EMA Hourly Continuation — WOO/USDT P100_200

**Symbol:** WOO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.5730 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8097 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -3.1434 |
| sortino_ratio | -0.8541 |
| max_drawdown | 0.6324 |
| cagr | -0.3287 |
| net_avg_win | 50.8232 |
| net_avg_loss | -74.4304 |
| avg_hold_time_bars | 9.6749 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
