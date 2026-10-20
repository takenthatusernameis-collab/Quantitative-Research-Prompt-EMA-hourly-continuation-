# EMA Hourly Continuation — ROSE/USDT P20_26

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1313 |
| net_profit_factor | 0.2743 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -13.3313 |
| sortino_ratio | -6.9364 |
| max_drawdown | 0.9999 |
| cagr | -0.9728 |
| net_avg_win | 7.4399 |
| net_avg_loss | -17.1159 |
| avg_hold_time_bars | 1.9589 |
| exposure | 0.1169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
