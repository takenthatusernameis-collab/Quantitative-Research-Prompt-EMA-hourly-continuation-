# EMA Hourly Continuation — SUSHI/USDT P12_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.3478 |
| net_win_rate | 0.4146 |
| gross_profit_factor | 0.7838 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -11.5505 |
| sortino_ratio | -6.1465 |
| max_drawdown | 0.9996 |
| cagr | -0.9552 |
| net_avg_win | 9.0354 |
| net_avg_loss | -18.3996 |
| avg_hold_time_bars | 2.8967 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
