# EMA Hourly Continuation — CELO/USDT P8_20

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -3.6737 |
| sortino_ratio | -1.3348 |
| max_drawdown | 0.7874 |
| cagr | -0.4582 |
| net_avg_win | 49.8895 |
| net_avg_loss | -68.8888 |
| avg_hold_time_bars | 5.2272 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
