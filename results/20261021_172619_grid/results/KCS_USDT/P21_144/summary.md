# EMA Hourly Continuation — KCS/USDT P21_144

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -3.5575 |
| sortino_ratio | -0.9849 |
| max_drawdown | 0.6868 |
| cagr | -0.3641 |
| net_avg_win | 53.8712 |
| net_avg_loss | -78.4496 |
| avg_hold_time_bars | 29.6160 |
| exposure | 0.5048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
