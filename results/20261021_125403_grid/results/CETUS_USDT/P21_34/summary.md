# EMA Hourly Continuation — CETUS/USDT P21_34

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6734 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.9368 |
| sortino_ratio | -0.8116 |
| max_drawdown | 0.6378 |
| cagr | -0.3119 |
| net_avg_win | 72.7630 |
| net_avg_loss | -91.6335 |
| avg_hold_time_bars | 4.8488 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
