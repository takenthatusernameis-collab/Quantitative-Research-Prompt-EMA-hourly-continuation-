# EMA Hourly Continuation — FLR/USDT P89_100

**Symbol:** FLR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 112 |
| net_profit_factor | 0.5107 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7544 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.2303 |
| sortino_ratio | -0.3375 |
| max_drawdown | 0.3347 |
| cagr | -0.1441 |
| net_avg_win | 70.3358 |
| net_avg_loss | -103.3020 |
| avg_hold_time_bars | 5.1696 |
| exposure | 0.0263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
