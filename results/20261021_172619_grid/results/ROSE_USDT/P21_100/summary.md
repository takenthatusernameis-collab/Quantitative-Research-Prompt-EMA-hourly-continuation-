# EMA Hourly Continuation — ROSE/USDT P21_100

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8247 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.4624 |
| sortino_ratio | -0.4596 |
| max_drawdown | 0.5037 |
| cagr | -0.1921 |
| net_avg_win | 80.9799 |
| net_avg_loss | -97.7851 |
| avg_hold_time_bars | 19.1843 |
| exposure | 0.4212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
