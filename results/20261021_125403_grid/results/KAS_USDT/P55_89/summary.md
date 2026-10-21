# EMA Hourly Continuation — KAS/USDT P55_89

**Symbol:** KAS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.1770 |
| sortino_ratio | -0.4993 |
| max_drawdown | 0.4367 |
| cagr | -0.2043 |
| net_avg_win | 61.9671 |
| net_avg_loss | -86.6096 |
| avg_hold_time_bars | 7.0116 |
| exposure | 0.0822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
