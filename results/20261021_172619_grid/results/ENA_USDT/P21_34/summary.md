# EMA Hourly Continuation — ENA/USDT P21_34

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9507 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.3152 |
| sortino_ratio | -0.3096 |
| max_drawdown | 0.3533 |
| cagr | -0.1328 |
| net_avg_win | 66.8246 |
| net_avg_loss | -87.9552 |
| avg_hold_time_bars | 5.1037 |
| exposure | 0.0626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
