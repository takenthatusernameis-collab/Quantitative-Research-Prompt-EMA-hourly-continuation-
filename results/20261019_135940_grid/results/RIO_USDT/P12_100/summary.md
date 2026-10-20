# EMA Hourly Continuation — RIO/USDT P12_100

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -4.3252 |
| sortino_ratio | -1.7337 |
| max_drawdown | 0.8811 |
| cagr | -0.5643 |
| net_avg_win | 41.7743 |
| net_avg_loss | -54.2264 |
| avg_hold_time_bars | 14.7244 |
| exposure | 0.5469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
