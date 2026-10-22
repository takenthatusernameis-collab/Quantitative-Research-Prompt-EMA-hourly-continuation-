# EMA Hourly Continuation — ZRO/USDT P12_50

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0715 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -3.9479 |
| sortino_ratio | -1.8313 |
| max_drawdown | 0.8763 |
| cagr | -0.5842 |
| net_avg_win | 41.7463 |
| net_avg_loss | -60.1921 |
| avg_hold_time_bars | 7.0269 |
| exposure | 0.3457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
