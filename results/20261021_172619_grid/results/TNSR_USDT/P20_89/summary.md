# EMA Hourly Continuation — TNSR/USDT P20_89

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.8641 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0667 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.0642 |
| sortino_ratio | -0.3524 |
| max_drawdown | 0.4019 |
| cagr | -0.1526 |
| net_avg_win | 78.6617 |
| net_avg_loss | -97.7636 |
| avg_hold_time_bars | 15.5610 |
| exposure | 0.3753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
