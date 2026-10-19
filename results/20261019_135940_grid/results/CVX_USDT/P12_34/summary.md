# EMA Hourly Continuation — CVX/USDT P12_34

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1294 |
| net_profit_factor | 0.4549 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.7787 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -8.3494 |
| sortino_ratio | -4.2326 |
| max_drawdown | 0.9945 |
| cagr | -0.8729 |
| net_avg_win | 14.4836 |
| net_avg_loss | -25.3021 |
| avg_hold_time_bars | 4.1383 |
| exposure | 0.2434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
