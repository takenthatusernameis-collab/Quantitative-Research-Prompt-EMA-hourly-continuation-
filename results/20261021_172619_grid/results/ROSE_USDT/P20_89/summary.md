# EMA Hourly Continuation — ROSE/USDT P20_89

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8115 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.6073 |
| sortino_ratio | -0.5143 |
| max_drawdown | 0.5065 |
| cagr | -0.2121 |
| net_avg_win | 78.1673 |
| net_avg_loss | -94.0521 |
| avg_hold_time_bars | 17.2490 |
| exposure | 0.3936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
