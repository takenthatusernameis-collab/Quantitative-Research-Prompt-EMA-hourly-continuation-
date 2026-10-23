# EMA Hourly Continuation — OGN/USDT P21_55

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.5106 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -7.4382 |
| sortino_ratio | -3.1982 |
| max_drawdown | 0.9816 |
| cagr | -0.7917 |
| net_avg_win | 24.6636 |
| net_avg_loss | -38.1796 |
| avg_hold_time_bars | 5.7511 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
