# EMA Hourly Continuation — SWFTC/USDT P26_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.8650 |
| sortino_ratio | -0.5106 |
| max_drawdown | 0.4591 |
| cagr | -0.2078 |
| net_avg_win | 65.2596 |
| net_avg_loss | -87.4356 |
| avg_hold_time_bars | 8.1205 |
| exposure | 0.1347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
