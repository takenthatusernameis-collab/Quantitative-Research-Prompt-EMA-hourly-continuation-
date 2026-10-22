# EMA Hourly Continuation — FIDA/USDT P26_55

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0326 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -2.0134 |
| sortino_ratio | -0.6408 |
| max_drawdown | 0.5532 |
| cagr | -0.2545 |
| net_avg_win | 63.3075 |
| net_avg_loss | -87.2845 |
| avg_hold_time_bars | 8.0791 |
| exposure | 0.1802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
