# EMA Hourly Continuation — BCH/USDT P8_21

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6356 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.1072 |
| sortino_ratio | -0.9549 |
| max_drawdown | 0.6751 |
| cagr | -0.3530 |
| net_avg_win | 52.2422 |
| net_avg_loss | -77.3180 |
| avg_hold_time_bars | 6.7096 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
