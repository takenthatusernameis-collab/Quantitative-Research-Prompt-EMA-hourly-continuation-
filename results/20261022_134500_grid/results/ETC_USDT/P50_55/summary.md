# EMA Hourly Continuation — ETC/USDT P50_55

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.1218 |
| net_win_rate | 0.3070 |
| gross_profit_factor | 0.6461 |
| gross_win_rate | 0.4223 |
| sharpe_ratio | -14.0923 |
| sortino_ratio | -6.1584 |
| max_drawdown | 0.9998 |
| cagr | -0.9660 |
| net_avg_win | 5.4794 |
| net_avg_loss | -19.9374 |
| avg_hold_time_bars | 1.8604 |
| exposure | 0.0697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
