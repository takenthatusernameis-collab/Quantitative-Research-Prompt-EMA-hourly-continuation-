# EMA Hourly Continuation — RSR/USDT P20_50

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.5425 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -6.2311 |
| sortino_ratio | -2.7150 |
| max_drawdown | 0.9643 |
| cagr | -0.7315 |
| net_avg_win | 26.1324 |
| net_avg_loss | -40.5623 |
| avg_hold_time_bars | 4.9812 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
