# EMA Hourly Continuation — AUCTION/USDT P12_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6441 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -4.4343 |
| sortino_ratio | -1.6346 |
| max_drawdown | 0.8582 |
| cagr | -0.5340 |
| net_avg_win | 50.3472 |
| net_avg_loss | -64.5132 |
| avg_hold_time_bars | 11.7128 |
| exposure | 0.3599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
