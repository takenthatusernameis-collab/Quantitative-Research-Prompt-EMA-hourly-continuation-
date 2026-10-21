# EMA Hourly Continuation — SWFTC/USDT P8_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7480 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -2.3787 |
| sortino_ratio | -0.8080 |
| max_drawdown | 0.6100 |
| cagr | -0.3105 |
| net_avg_win | 67.2191 |
| net_avg_loss | -79.4849 |
| avg_hold_time_bars | 19.9282 |
| exposure | 0.5172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
