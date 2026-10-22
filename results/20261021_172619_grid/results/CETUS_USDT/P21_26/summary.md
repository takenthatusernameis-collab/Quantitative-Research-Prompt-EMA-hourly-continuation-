# EMA Hourly Continuation — CETUS/USDT P21_26

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.7101 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 1.0320 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.8792 |
| sortino_ratio | -0.4194 |
| max_drawdown | 0.4207 |
| cagr | -0.1754 |
| net_avg_win | 77.9817 |
| net_avg_loss | -108.9201 |
| avg_hold_time_bars | 4.3663 |
| exposure | 0.0480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
