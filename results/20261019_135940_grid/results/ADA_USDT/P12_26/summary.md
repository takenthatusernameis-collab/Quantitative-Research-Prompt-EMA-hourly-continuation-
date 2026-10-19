# EMA Hourly Continuation — ADA/USDT P12_26

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1410 |
| net_profit_factor | 0.3178 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -12.1780 |
| sortino_ratio | -6.4918 |
| max_drawdown | 0.9998 |
| cagr | -0.9643 |
| net_avg_win | 7.9486 |
| net_avg_loss | -17.7859 |
| avg_hold_time_bars | 2.6177 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
