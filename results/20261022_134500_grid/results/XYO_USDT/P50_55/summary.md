# EMA Hourly Continuation — XYO/USDT P50_55

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.1431 |
| net_win_rate | 0.2790 |
| gross_profit_factor | 0.5490 |
| gross_win_rate | 0.3498 |
| sharpe_ratio | -15.6437 |
| sortino_ratio | -7.2206 |
| max_drawdown | 1.0000 |
| cagr | -0.9817 |
| net_avg_win | 6.4252 |
| net_avg_loss | -17.3663 |
| avg_hold_time_bars | 2.4024 |
| exposure | 0.1013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
