# EMA Hourly Continuation — CELO/USDT P21_55

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6391 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8554 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.1473 |
| sortino_ratio | -1.0483 |
| max_drawdown | 0.7085 |
| cagr | -0.3814 |
| net_avg_win | 48.5756 |
| net_avg_loss | -66.6361 |
| avg_hold_time_bars | 9.0456 |
| exposure | 0.2243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
