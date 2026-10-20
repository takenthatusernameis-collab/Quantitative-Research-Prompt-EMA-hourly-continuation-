# EMA Hourly Continuation — MERL/USDT P100_200

**Symbol:** MERL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.7206 |
| gross_win_rate | 0.4100 |
| sharpe_ratio | -3.9876 |
| sortino_ratio | -1.0591 |
| max_drawdown | 0.7360 |
| cagr | -0.4019 |
| net_avg_win | 56.8897 |
| net_avg_loss | -72.9079 |
| avg_hold_time_bars | 9.8504 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
