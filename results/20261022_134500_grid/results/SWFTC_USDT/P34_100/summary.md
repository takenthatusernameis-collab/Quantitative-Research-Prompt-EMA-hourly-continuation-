# EMA Hourly Continuation — SWFTC/USDT P34_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.4941 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -6.1361 |
| sortino_ratio | -2.1344 |
| max_drawdown | 0.9321 |
| cagr | -0.6574 |
| net_avg_win | 34.3546 |
| net_avg_loss | -51.9015 |
| avg_hold_time_bars | 9.7613 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
