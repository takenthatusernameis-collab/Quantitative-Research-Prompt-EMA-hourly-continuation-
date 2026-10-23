# EMA Hourly Continuation — KSM/USDT P12_21

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.3096 |
| net_win_rate | 0.4103 |
| gross_profit_factor | 0.8778 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -13.0482 |
| sortino_ratio | -7.1945 |
| max_drawdown | 0.9999 |
| cagr | -0.9737 |
| net_avg_win | 7.3396 |
| net_avg_loss | -16.4959 |
| avg_hold_time_bars | 2.4976 |
| exposure | 0.1690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
