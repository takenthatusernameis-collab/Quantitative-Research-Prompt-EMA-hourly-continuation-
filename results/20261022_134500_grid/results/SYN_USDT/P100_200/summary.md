# EMA Hourly Continuation — SYN/USDT P100_200

**Symbol:** SYN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.5107 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.7548 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -3.7383 |
| sortino_ratio | -1.0299 |
| max_drawdown | 0.7197 |
| cagr | -0.3890 |
| net_avg_win | 43.8325 |
| net_avg_loss | -67.4662 |
| avg_hold_time_bars | 12.0052 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
