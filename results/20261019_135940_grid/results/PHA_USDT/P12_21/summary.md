# EMA Hourly Continuation — PHA/USDT P12_21

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1457 |
| net_profit_factor | 0.3602 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8720 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -10.7117 |
| sortino_ratio | -5.7551 |
| max_drawdown | 0.9993 |
| cagr | -0.9460 |
| net_avg_win | 8.8733 |
| net_avg_loss | -18.9782 |
| avg_hold_time_bars | 2.4647 |
| exposure | 0.1632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
