# EMA Hourly Continuation — SNX/USDT P8_55

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7728 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.0360 |
| sortino_ratio | -0.7631 |
| max_drawdown | 0.6194 |
| cagr | -0.2969 |
| net_avg_win | 58.5612 |
| net_avg_loss | -74.6827 |
| avg_hold_time_bars | 14.5486 |
| exposure | 0.4536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
