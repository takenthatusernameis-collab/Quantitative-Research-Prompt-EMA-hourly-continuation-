# EMA Hourly Continuation — FET/USDT P55_100

**Symbol:** FET/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -4.2201 |
| sortino_ratio | -1.4221 |
| max_drawdown | 0.8339 |
| cagr | -0.5037 |
| net_avg_win | 36.5410 |
| net_avg_loss | -60.6873 |
| avg_hold_time_bars | 5.7333 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
