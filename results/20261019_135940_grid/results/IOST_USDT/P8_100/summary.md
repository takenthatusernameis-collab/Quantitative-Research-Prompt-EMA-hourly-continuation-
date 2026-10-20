# EMA Hourly Continuation — IOST/USDT P8_100

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6669 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -3.2223 |
| sortino_ratio | -1.1206 |
| max_drawdown | 0.7621 |
| cagr | -0.4173 |
| net_avg_win | 49.5547 |
| net_avg_loss | -72.1380 |
| avg_hold_time_bars | 24.8489 |
| exposure | 0.6879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
