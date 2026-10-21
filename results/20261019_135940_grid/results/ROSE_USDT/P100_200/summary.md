# EMA Hourly Continuation — ROSE/USDT P100_200

**Symbol:** ROSE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9679 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5652 |
| sortino_ratio | -0.7245 |
| max_drawdown | 0.5881 |
| cagr | -0.2930 |
| net_avg_win | 54.3212 |
| net_avg_loss | -81.2242 |
| avg_hold_time_bars | 8.7562 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
