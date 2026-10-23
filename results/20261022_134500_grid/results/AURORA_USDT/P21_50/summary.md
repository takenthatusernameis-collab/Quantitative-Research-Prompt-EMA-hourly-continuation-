# EMA Hourly Continuation — AURORA/USDT P21_50

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 788 |
| net_profit_factor | 0.4070 |
| net_win_rate | 0.3997 |
| gross_profit_factor | 0.8313 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -8.5701 |
| sortino_ratio | -3.4069 |
| max_drawdown | 0.9876 |
| cagr | -0.8215 |
| net_avg_win | 21.5041 |
| net_avg_loss | -35.1836 |
| avg_hold_time_bars | 6.4848 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
