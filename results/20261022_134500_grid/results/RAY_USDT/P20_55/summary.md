# EMA Hourly Continuation — RAY/USDT P20_55

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -6.1731 |
| sortino_ratio | -2.5995 |
| max_drawdown | 0.9594 |
| cagr | -0.7179 |
| net_avg_win | 31.9401 |
| net_avg_loss | -45.8718 |
| avg_hold_time_bars | 5.8801 |
| exposure | 0.2408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
