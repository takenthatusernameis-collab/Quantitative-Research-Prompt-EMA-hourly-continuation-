# EMA Hourly Continuation — QNT/USDT P34_100

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 789 |
| net_profit_factor | 0.5000 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -5.9569 |
| sortino_ratio | -2.3582 |
| max_drawdown | 0.9453 |
| cagr | -0.6801 |
| net_avg_win | 26.1177 |
| net_avg_loss | -44.0586 |
| avg_hold_time_bars | 6.8428 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
