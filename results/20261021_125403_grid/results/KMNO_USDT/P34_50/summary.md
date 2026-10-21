# EMA Hourly Continuation — KMNO/USDT P34_50

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.7216 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0410 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.8582 |
| sortino_ratio | -0.4594 |
| max_drawdown | 0.4201 |
| cagr | -0.1926 |
| net_avg_win | 71.4331 |
| net_avg_loss | -101.7293 |
| avg_hold_time_bars | 4.7075 |
| exposure | 0.0639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
