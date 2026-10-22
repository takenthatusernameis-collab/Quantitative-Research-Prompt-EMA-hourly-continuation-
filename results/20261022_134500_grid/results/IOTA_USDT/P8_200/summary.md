# EMA Hourly Continuation — IOTA/USDT P8_200

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7740 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0909 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -1.5488 |
| sortino_ratio | -0.4212 |
| max_drawdown | 0.4273 |
| cagr | -0.1834 |
| net_avg_win | 71.5158 |
| net_avg_loss | -96.4371 |
| avg_hold_time_bars | 47.7299 |
| exposure | 0.8114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
