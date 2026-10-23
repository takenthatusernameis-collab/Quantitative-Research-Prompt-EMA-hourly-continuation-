# EMA Hourly Continuation — WAVES/USDT P100_200

**Symbol:** WAVES/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.3809 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.6958 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -6.1260 |
| sortino_ratio | -1.8870 |
| max_drawdown | 0.9154 |
| cagr | -0.6194 |
| net_avg_win | 28.4743 |
| net_avg_loss | -51.1310 |
| avg_hold_time_bars | 7.7938 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
