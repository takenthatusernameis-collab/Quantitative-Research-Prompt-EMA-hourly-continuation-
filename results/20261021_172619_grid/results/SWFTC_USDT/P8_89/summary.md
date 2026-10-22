# EMA Hourly Continuation — SWFTC/USDT P8_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.7938 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9674 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -1.9096 |
| sortino_ratio | -0.6688 |
| max_drawdown | 0.5477 |
| cagr | -0.2653 |
| net_avg_win | 70.5693 |
| net_avg_loss | -84.8603 |
| avg_hold_time_bars | 18.2342 |
| exposure | 0.4990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
