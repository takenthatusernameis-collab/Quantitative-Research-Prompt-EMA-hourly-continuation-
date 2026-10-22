# EMA Hourly Continuation — ETC/USDT P26_55

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.3746 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -9.0405 |
| sortino_ratio | -3.9323 |
| max_drawdown | 0.9929 |
| cagr | -0.8605 |
| net_avg_win | 14.7598 |
| net_avg_loss | -29.6215 |
| avg_hold_time_bars | 3.9329 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
