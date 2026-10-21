# EMA Hourly Continuation — GMX/USDT P20_26

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -3.5028 |
| sortino_ratio | -0.9339 |
| max_drawdown | 0.6624 |
| cagr | -0.3489 |
| net_avg_win | 53.4702 |
| net_avg_loss | -81.1673 |
| avg_hold_time_bars | 5.3623 |
| exposure | 0.0841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
