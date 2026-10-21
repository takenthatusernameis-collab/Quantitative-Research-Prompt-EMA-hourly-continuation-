# EMA Hourly Continuation — BAT/USDT P12_55

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6882 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -3.2986 |
| sortino_ratio | -1.2412 |
| max_drawdown | 0.7650 |
| cagr | -0.4344 |
| net_avg_win | 50.5938 |
| net_avg_loss | -67.2348 |
| avg_hold_time_bars | 11.5957 |
| exposure | 0.3663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
