# EMA Hourly Continuation — DAG/USDT P8_20

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -2.4733 |
| sortino_ratio | -0.6218 |
| max_drawdown | 0.5367 |
| cagr | -0.2483 |
| net_avg_win | 60.9734 |
| net_avg_loss | -79.2698 |
| avg_hold_time_bars | 7.2452 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
