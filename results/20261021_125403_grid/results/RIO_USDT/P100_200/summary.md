# EMA Hourly Continuation — RIO/USDT P100_200

**Symbol:** RIO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.6299 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7316 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -2.3325 |
| sortino_ratio | -0.5389 |
| max_drawdown | 0.4806 |
| cagr | -0.2206 |
| net_avg_win | 69.5739 |
| net_avg_loss | -81.5750 |
| avg_hold_time_bars | 12.9098 |
| exposure | 0.1577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
