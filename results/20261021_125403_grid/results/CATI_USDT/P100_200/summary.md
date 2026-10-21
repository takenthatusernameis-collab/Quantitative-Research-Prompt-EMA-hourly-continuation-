# EMA Hourly Continuation — CATI/USDT P100_200

**Symbol:** CATI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.5409 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.6681 |
| gross_win_rate | 0.4028 |
| sharpe_ratio | -3.0043 |
| sortino_ratio | -0.6753 |
| max_drawdown | 0.4826 |
| cagr | -0.2679 |
| net_avg_win | 66.1962 |
| net_avg_loss | -82.5602 |
| avg_hold_time_bars | 12.4692 |
| exposure | 0.1442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
