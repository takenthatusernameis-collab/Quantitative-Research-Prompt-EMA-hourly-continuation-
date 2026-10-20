# EMA Hourly Continuation — GMX/USDT P89_100

**Symbol:** GMX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.2853 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.8294 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -8.5723 |
| sortino_ratio | -3.0707 |
| max_drawdown | 0.9808 |
| cagr | -0.7917 |
| net_avg_win | 15.3502 |
| net_avg_loss | -37.8998 |
| avg_hold_time_bars | 2.7601 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
