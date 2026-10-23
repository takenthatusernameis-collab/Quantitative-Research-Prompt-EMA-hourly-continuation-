# EMA Hourly Continuation — PHA/USDT P50_200

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6412 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -2.8160 |
| sortino_ratio | -0.8308 |
| max_drawdown | 0.6317 |
| cagr | -0.3214 |
| net_avg_win | 55.3324 |
| net_avg_loss | -74.1243 |
| avg_hold_time_bars | 17.4782 |
| exposure | 0.3456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
