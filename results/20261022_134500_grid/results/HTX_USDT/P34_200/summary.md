# EMA Hourly Continuation — HTX/USDT P34_200

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.4058 |
| net_win_rate | 0.3750 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -7.3961 |
| sortino_ratio | -2.1366 |
| max_drawdown | 0.9465 |
| cagr | -0.6852 |
| net_avg_win | 41.4138 |
| net_avg_loss | -61.2265 |
| avg_hold_time_bars | 28.7043 |
| exposure | 0.5404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
