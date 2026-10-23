# EMA Hourly Continuation — BRETT/USDT P8_12

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1735 |
| net_profit_factor | 0.3212 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.7059 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -14.2286 |
| sortino_ratio | -8.6139 |
| max_drawdown | 1.0000 |
| cagr | -0.9886 |
| net_avg_win | 6.7301 |
| net_avg_loss | -14.2743 |
| avg_hold_time_bars | 1.9159 |
| exposure | 0.1599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
