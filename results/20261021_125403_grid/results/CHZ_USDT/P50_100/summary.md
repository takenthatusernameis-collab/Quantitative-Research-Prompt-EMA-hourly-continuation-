# EMA Hourly Continuation — CHZ/USDT P50_100

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.6844 |
| sortino_ratio | -0.4425 |
| max_drawdown | 0.4331 |
| cagr | -0.1844 |
| net_avg_win | 71.8204 |
| net_avg_loss | -95.6642 |
| avg_hold_time_bars | 9.7173 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
