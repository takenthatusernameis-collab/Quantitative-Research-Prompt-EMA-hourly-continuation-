# EMA Hourly Continuation — RUNE/USDT P21_50

**Symbol:** RUNE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7459 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0268 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.1944 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5549 |
| cagr | -0.2726 |
| net_avg_win | 65.3870 |
| net_avg_loss | -89.1101 |
| avg_hold_time_bars | 7.2980 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
