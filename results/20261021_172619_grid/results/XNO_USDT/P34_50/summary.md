# EMA Hourly Continuation — XNO/USDT P34_50

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -2.7548 |
| sortino_ratio | -0.6384 |
| max_drawdown | 0.5472 |
| cagr | -0.2549 |
| net_avg_win | 62.0667 |
| net_avg_loss | -86.9679 |
| avg_hold_time_bars | 5.2311 |
| exposure | 0.0628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
