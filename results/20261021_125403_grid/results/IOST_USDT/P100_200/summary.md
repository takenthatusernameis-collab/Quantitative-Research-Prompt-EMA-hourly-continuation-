# EMA Hourly Continuation — IOST/USDT P100_200

**Symbol:** IOST/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8342 |
| net_win_rate | 0.5395 |
| gross_profit_factor | 1.1617 |
| gross_win_rate | 0.5395 |
| sharpe_ratio | -0.9544 |
| sortino_ratio | -0.2405 |
| max_drawdown | 0.2993 |
| cagr | -0.1061 |
| net_avg_win | 75.3542 |
| net_avg_loss | -105.8110 |
| avg_hold_time_bars | 11.7336 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
