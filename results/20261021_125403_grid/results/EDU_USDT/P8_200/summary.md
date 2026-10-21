# EMA Hourly Continuation — EDU/USDT P8_200

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8541 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -1.9174 |
| sortino_ratio | -0.5398 |
| max_drawdown | 0.4897 |
| cagr | -0.2211 |
| net_avg_win | 72.0009 |
| net_avg_loss | -83.4205 |
| avg_hold_time_bars | 41.7809 |
| exposure | 0.7506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
