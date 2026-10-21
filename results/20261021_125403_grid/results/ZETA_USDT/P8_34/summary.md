# EMA Hourly Continuation — ZETA/USDT P8_34

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.7589 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.5348 |
| sortino_ratio | -0.9894 |
| max_drawdown | 0.6924 |
| cagr | -0.3655 |
| net_avg_win | 57.9172 |
| net_avg_loss | -75.2998 |
| avg_hold_time_bars | 10.1084 |
| exposure | 0.3417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
