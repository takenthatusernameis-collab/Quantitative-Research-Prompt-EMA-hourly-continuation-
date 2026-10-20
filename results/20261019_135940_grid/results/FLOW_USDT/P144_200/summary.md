# EMA Hourly Continuation — FLOW/USDT P144_200

**Symbol:** FLOW/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.4500 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8562 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -5.1643 |
| sortino_ratio | -1.4844 |
| max_drawdown | 0.8384 |
| cagr | -0.5145 |
| net_avg_win | 38.4706 |
| net_avg_loss | -65.5977 |
| avg_hold_time_bars | 4.5049 |
| exposure | 0.0840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
