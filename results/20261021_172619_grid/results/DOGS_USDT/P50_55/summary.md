# EMA Hourly Continuation — DOGS/USDT P50_55

**Symbol:** DOGS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 0.6780 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.0900 |
| sortino_ratio | -0.1465 |
| max_drawdown | 0.1603 |
| cagr | -0.0650 |
| net_avg_win | 78.8018 |
| net_avg_loss | -104.5972 |
| avg_hold_time_bars | 6.1053 |
| exposure | 0.0246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
