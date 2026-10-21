# EMA Hourly Continuation — MOCA/USDT P50_100

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7485 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.7825 |
| sortino_ratio | -0.4899 |
| max_drawdown | 0.4371 |
| cagr | -0.2019 |
| net_avg_win | 71.9831 |
| net_avg_loss | -95.0299 |
| avg_hold_time_bars | 9.0689 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
