# EMA Hourly Continuation — HTX/USDT P21_100

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.3399 |
| net_win_rate | 0.3434 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4097 |
| sharpe_ratio | -10.7390 |
| sortino_ratio | -4.1639 |
| max_drawdown | 0.9964 |
| cagr | -0.8924 |
| net_avg_win | 20.6020 |
| net_avg_loss | -31.7096 |
| avg_hold_time_bars | 14.0524 |
| exposure | 0.4610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
