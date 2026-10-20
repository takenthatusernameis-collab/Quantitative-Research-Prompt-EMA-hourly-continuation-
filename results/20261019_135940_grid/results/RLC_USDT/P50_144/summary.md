# EMA Hourly Continuation — RLC/USDT P50_144

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8943 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -3.8097 |
| sortino_ratio | -1.1960 |
| max_drawdown | 0.7737 |
| cagr | -0.4369 |
| net_avg_win | 45.1813 |
| net_avg_loss | -67.0994 |
| avg_hold_time_bars | 13.1670 |
| exposure | 0.2975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
