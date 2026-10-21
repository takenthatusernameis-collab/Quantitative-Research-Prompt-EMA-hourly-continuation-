# EMA Hourly Continuation — BRETT/USDT P144_200

**Symbol:** BRETT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.7752 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9558 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.0917 |
| sortino_ratio | -0.2093 |
| max_drawdown | 0.2428 |
| cagr | -0.0921 |
| net_avg_win | 85.1580 |
| net_avg_loss | -104.7970 |
| avg_hold_time_bars | 7.2824 |
| exposure | 0.0596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
