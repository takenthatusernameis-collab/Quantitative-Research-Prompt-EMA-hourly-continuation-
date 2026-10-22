# EMA Hourly Continuation — TRAC/USDT P50_200

**Symbol:** TRAC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6974 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.1525 |
| sortino_ratio | -0.6076 |
| max_drawdown | 0.5203 |
| cagr | -0.2479 |
| net_avg_win | 59.4818 |
| net_avg_loss | -84.0191 |
| avg_hold_time_bars | 20.9248 |
| exposure | 0.3795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
