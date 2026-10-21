# EMA Hourly Continuation — NEAR/USDT P8_100

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.1261 |
| sortino_ratio | -0.3491 |
| max_drawdown | 0.3783 |
| cagr | -0.1510 |
| net_avg_win | 70.9175 |
| net_avg_loss | -85.6294 |
| avg_hold_time_bars | 30.9041 |
| exposure | 0.6588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
