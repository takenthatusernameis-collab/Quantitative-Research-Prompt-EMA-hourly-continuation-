# EMA Hourly Continuation — AURORA/USDT P8_26

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6283 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -4.9810 |
| sortino_ratio | -1.8368 |
| max_drawdown | 0.8890 |
| cagr | -0.5738 |
| net_avg_win | 49.7273 |
| net_avg_loss | -64.6968 |
| avg_hold_time_bars | 7.2504 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
