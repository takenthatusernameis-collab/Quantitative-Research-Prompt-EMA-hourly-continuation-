# EMA Hourly Continuation — LUNC/USDT P12_100

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 806 |
| net_profit_factor | 0.4574 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.7658 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -6.1826 |
| sortino_ratio | -2.4631 |
| max_drawdown | 0.9515 |
| cagr | -0.6956 |
| net_avg_win | 22.6105 |
| net_avg_loss | -38.7163 |
| avg_hold_time_bars | 13.8226 |
| exposure | 0.5064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
