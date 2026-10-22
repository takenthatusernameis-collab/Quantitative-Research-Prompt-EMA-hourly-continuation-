# EMA Hourly Continuation — DOGS/USDT P26_100

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8150 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.2602 |
| sortino_ratio | -0.3782 |
| max_drawdown | 0.3211 |
| cagr | -0.1610 |
| net_avg_win | 73.3322 |
| net_avg_loss | -90.9372 |
| avg_hold_time_bars | 17.0559 |
| exposure | 0.3402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
