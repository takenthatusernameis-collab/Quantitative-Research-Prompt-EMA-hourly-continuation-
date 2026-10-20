# EMA Hourly Continuation — ELON/USDT P50_89

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.3635 |
| net_win_rate | 0.4092 |
| gross_profit_factor | 0.6849 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -7.3953 |
| sortino_ratio | -2.6924 |
| max_drawdown | 0.9641 |
| cagr | -0.7301 |
| net_avg_win | 20.6726 |
| net_avg_loss | -39.3909 |
| avg_hold_time_bars | 4.4323 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
