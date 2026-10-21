# EMA Hourly Continuation — LPT/USDT P34_55

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -3.4137 |
| sortino_ratio | -0.9895 |
| max_drawdown | 0.6861 |
| cagr | -0.3658 |
| net_avg_win | 54.4364 |
| net_avg_loss | -76.1062 |
| avg_hold_time_bars | 5.8762 |
| exposure | 0.1100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
