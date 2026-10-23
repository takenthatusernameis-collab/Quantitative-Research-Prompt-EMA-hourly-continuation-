# EMA Hourly Continuation — XAI/USDT P50_144

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9369 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -3.0557 |
| sortino_ratio | -0.9620 |
| max_drawdown | 0.7276 |
| cagr | -0.3658 |
| net_avg_win | 58.5442 |
| net_avg_loss | -79.5688 |
| avg_hold_time_bars | 15.5372 |
| exposure | 0.3510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
