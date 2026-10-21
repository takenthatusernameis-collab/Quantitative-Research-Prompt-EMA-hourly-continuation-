# EMA Hourly Continuation — PUFFER/USDT P12_21

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8742 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -3.1727 |
| sortino_ratio | -0.9131 |
| max_drawdown | 0.6091 |
| cagr | -0.3448 |
| net_avg_win | 67.0612 |
| net_avg_loss | -88.7464 |
| avg_hold_time_bars | 5.8933 |
| exposure | 0.1094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
