# EMA Hourly Continuation — XDC/USDT P21_100

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.3039 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.7298 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -7.8005 |
| sortino_ratio | -3.0674 |
| max_drawdown | 0.9839 |
| cagr | -0.8050 |
| net_avg_win | 12.1615 |
| net_avg_loss | -31.0509 |
| avg_hold_time_bars | 9.7290 |
| exposure | 0.3573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
