# EMA Hourly Continuation — CTSI/USDT P12_26

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.8752 |
| sortino_ratio | -1.3707 |
| max_drawdown | 0.7923 |
| cagr | -0.4651 |
| net_avg_win | 49.0192 |
| net_avg_loss | -68.0839 |
| avg_hold_time_bars | 5.9754 |
| exposure | 0.1657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
