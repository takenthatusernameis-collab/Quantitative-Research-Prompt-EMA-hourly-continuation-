# EMA Hourly Continuation — XDC/USDT P50_55

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1528 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | -1.1561 |
| sortino_ratio | -0.1735 |
| max_drawdown | 0.1974 |
| cagr | -0.0770 |
| net_avg_win | 70.4520 |
| net_avg_loss | -118.1942 |
| avg_hold_time_bars | 6.0463 |
| exposure | 0.0297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
