# EMA Hourly Continuation — RUNE/USDT P55_100

**Symbol:** RUNE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.5540 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9387 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -3.9388 |
| sortino_ratio | -1.3612 |
| max_drawdown | 0.8094 |
| cagr | -0.4740 |
| net_avg_win | 34.0677 |
| net_avg_loss | -60.6598 |
| avg_hold_time_bars | 5.8061 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
