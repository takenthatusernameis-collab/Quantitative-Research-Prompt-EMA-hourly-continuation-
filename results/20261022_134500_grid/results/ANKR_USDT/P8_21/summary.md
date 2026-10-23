# EMA Hourly Continuation — ANKR/USDT P8_21

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1626 |
| net_profit_factor | 0.3366 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.7607 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -13.4344 |
| sortino_ratio | -7.6784 |
| max_drawdown | 0.9999 |
| cagr | -0.9802 |
| net_avg_win | 7.6871 |
| net_avg_loss | -15.6035 |
| avg_hold_time_bars | 3.3875 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
