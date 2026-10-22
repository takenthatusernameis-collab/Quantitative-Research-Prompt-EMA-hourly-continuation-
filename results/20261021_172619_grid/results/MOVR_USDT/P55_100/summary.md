# EMA Hourly Continuation — MOVR/USDT P55_100

**Symbol:** MOVR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.7497 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -3.4515 |
| sortino_ratio | -0.9418 |
| max_drawdown | 0.6820 |
| cagr | -0.3518 |
| net_avg_win | 54.1258 |
| net_avg_loss | -71.6315 |
| avg_hold_time_bars | 7.8351 |
| exposure | 0.1318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
