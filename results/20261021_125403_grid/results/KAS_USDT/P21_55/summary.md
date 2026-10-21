# EMA Hourly Continuation — KAS/USDT P21_55

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8593 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1235 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.9474 |
| sortino_ratio | -0.2953 |
| max_drawdown | 0.3467 |
| cagr | -0.1292 |
| net_avg_win | 72.2448 |
| net_avg_loss | -96.0888 |
| avg_hold_time_bars | 7.5591 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
