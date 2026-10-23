# EMA Hourly Continuation — PHA/USDT P50_55

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.1718 |
| net_win_rate | 0.3439 |
| gross_profit_factor | 0.5281 |
| gross_win_rate | 0.3910 |
| sharpe_ratio | -12.3674 |
| sortino_ratio | -5.2631 |
| max_drawdown | 0.9992 |
| cagr | -0.9407 |
| net_avg_win | 7.0998 |
| net_avg_loss | -21.6604 |
| avg_hold_time_bars | 1.7538 |
| exposure | 0.0677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
