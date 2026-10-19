# EMA Hourly Continuation — WLD/USDT P100_200

**Symbol:** WLD/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7551 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0695 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.5238 |
| sortino_ratio | -0.3839 |
| max_drawdown | 0.4078 |
| cagr | -0.1652 |
| net_avg_win | 70.2488 |
| net_avg_loss | -97.2894 |
| avg_hold_time_bars | 11.7700 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
