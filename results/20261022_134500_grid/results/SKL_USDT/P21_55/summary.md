# EMA Hourly Continuation — SKL/USDT P21_55

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.5270 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -6.5717 |
| sortino_ratio | -2.9275 |
| max_drawdown | 0.9724 |
| cagr | -0.7552 |
| net_avg_win | 23.6141 |
| net_avg_loss | -38.0063 |
| avg_hold_time_bars | 5.2244 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
