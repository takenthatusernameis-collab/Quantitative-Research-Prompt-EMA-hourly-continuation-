# EMA Hourly Continuation — HTX/USDT P55_200

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.4863 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.7464 |
| gross_win_rate | 0.3986 |
| sharpe_ratio | -4.5513 |
| sortino_ratio | -1.1185 |
| max_drawdown | 0.7454 |
| cagr | -0.4106 |
| net_avg_win | 59.0758 |
| net_avg_loss | -80.5358 |
| avg_hold_time_bars | 29.0541 |
| exposure | 0.3892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
