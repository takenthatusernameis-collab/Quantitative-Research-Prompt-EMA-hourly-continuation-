# EMA Hourly Continuation — HBAR/USDT P12_55

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.5635 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9561 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -6.9389 |
| sortino_ratio | -3.1938 |
| max_drawdown | 0.9812 |
| cagr | -0.7938 |
| net_avg_win | 25.3791 |
| net_avg_loss | -38.8159 |
| avg_hold_time_bars | 7.0724 |
| exposure | 0.3465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
