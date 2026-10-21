# EMA Hourly Continuation — XPR/USDT P20_21

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 78 |
| net_profit_factor | 0.8270 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1562 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.5019 |
| sortino_ratio | -0.0641 |
| max_drawdown | 0.1127 |
| cagr | -0.0294 |
| net_avg_win | 82.1650 |
| net_avg_loss | -115.9090 |
| avg_hold_time_bars | 18.0641 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
