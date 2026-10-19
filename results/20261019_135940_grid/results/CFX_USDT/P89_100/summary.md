# EMA Hourly Continuation — CFX/USDT P89_100

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.2726 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.7060 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -8.3643 |
| sortino_ratio | -2.8726 |
| max_drawdown | 0.9765 |
| cagr | -0.7755 |
| net_avg_win | 16.2645 |
| net_avg_loss | -38.4665 |
| avg_hold_time_bars | 2.2265 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
