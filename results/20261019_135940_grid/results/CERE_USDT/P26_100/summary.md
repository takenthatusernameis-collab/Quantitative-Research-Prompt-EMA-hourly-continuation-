# EMA Hourly Continuation — CERE/USDT P26_100

**Symbol:** CERE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.4611 |
| net_win_rate | 0.3652 |
| gross_profit_factor | 0.8024 |
| gross_win_rate | 0.3935 |
| sharpe_ratio | -9.1324 |
| sortino_ratio | -3.5111 |
| max_drawdown | 0.9904 |
| cagr | -0.8385 |
| net_avg_win | 31.2540 |
| net_avg_loss | -38.9960 |
| avg_hold_time_bars | 10.8113 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
