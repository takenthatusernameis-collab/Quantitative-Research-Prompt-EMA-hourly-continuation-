# EMA Hourly Continuation — IO/USDT P26_50

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.5561 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -6.3950 |
| sortino_ratio | -2.7976 |
| max_drawdown | 0.9619 |
| cagr | -0.7445 |
| net_avg_win | 28.7679 |
| net_avg_loss | -44.2215 |
| avg_hold_time_bars | 3.3506 |
| exposure | 0.1471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
