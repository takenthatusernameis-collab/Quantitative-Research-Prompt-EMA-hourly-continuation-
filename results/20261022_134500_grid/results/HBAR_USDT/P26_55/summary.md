# EMA Hourly Continuation — HBAR/USDT P26_55

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.4658 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -7.5379 |
| sortino_ratio | -3.1591 |
| max_drawdown | 0.9803 |
| cagr | -0.7891 |
| net_avg_win | 21.7386 |
| net_avg_loss | -38.2137 |
| avg_hold_time_bars | 4.1203 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
