# EMA Hourly Continuation — DYDX/USDT P8_26

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1560 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.9717 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -9.3878 |
| sortino_ratio | -5.2213 |
| max_drawdown | 0.9984 |
| cagr | -0.9218 |
| net_avg_win | 13.7441 |
| net_avg_loss | -22.9236 |
| avg_hold_time_bars | 3.8288 |
| exposure | 0.2715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
