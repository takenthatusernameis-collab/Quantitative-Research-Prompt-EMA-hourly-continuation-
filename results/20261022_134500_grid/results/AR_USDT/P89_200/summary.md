# EMA Hourly Continuation — AR/USDT P89_200

**Symbol:** AR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5566 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.8242 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.9699 |
| sortino_ratio | -1.0636 |
| max_drawdown | 0.7472 |
| cagr | -0.4050 |
| net_avg_win | 57.8807 |
| net_avg_loss | -77.8702 |
| avg_hold_time_bars | 10.9133 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
