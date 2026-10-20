# EMA Hourly Continuation — ROSE/USDT P8_34

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1427 |
| net_profit_factor | 0.5028 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8520 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -7.5945 |
| sortino_ratio | -4.0363 |
| max_drawdown | 0.9927 |
| cagr | -0.8586 |
| net_avg_win | 15.2578 |
| net_avg_loss | -25.9637 |
| avg_hold_time_bars | 5.3518 |
| exposure | 0.3471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
