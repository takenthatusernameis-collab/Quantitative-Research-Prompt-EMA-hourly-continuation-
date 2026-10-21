# EMA Hourly Continuation — CFX/USDT P100_200

**Symbol:** CFX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 233 |
| net_profit_factor | 0.7458 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -1.3844 |
| sortino_ratio | -0.3019 |
| max_drawdown | 0.2957 |
| cagr | -0.1297 |
| net_avg_win | 76.4740 |
| net_avg_loss | -96.5566 |
| avg_hold_time_bars | 15.8841 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
