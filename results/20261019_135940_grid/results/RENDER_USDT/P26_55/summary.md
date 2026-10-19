# EMA Hourly Continuation — RENDER/USDT P26_55

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.5112 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -6.7972 |
| sortino_ratio | -2.9610 |
| max_drawdown | 0.9587 |
| cagr | -0.7635 |
| net_avg_win | 26.6581 |
| net_avg_loss | -43.7456 |
| avg_hold_time_bars | 3.8637 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
