# EMA Hourly Continuation — CGPT/USDT P26_34

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.3011 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.8356 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -11.0097 |
| sortino_ratio | -4.9314 |
| max_drawdown | 0.9984 |
| cagr | -0.9218 |
| net_avg_win | 11.0841 |
| net_avg_loss | -24.3755 |
| avg_hold_time_bars | 2.1961 |
| exposure | 0.0972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
