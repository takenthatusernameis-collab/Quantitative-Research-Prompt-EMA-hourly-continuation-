# EMA Hourly Continuation — RSR/USDT P50_200

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.6822 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -2.3421 |
| sortino_ratio | -0.6376 |
| max_drawdown | 0.5385 |
| cagr | -0.2650 |
| net_avg_win | 63.8795 |
| net_avg_loss | -85.5933 |
| avg_hold_time_bars | 22.7230 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
