# EMA Hourly Continuation — ROSE/USDT P8_50

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.8673 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0745 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.3534 |
| sortino_ratio | -0.5232 |
| max_drawdown | 0.5499 |
| cagr | -0.2172 |
| net_avg_win | 80.4879 |
| net_avg_loss | -98.6197 |
| avg_hold_time_bars | 13.1851 |
| exposure | 0.4339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
