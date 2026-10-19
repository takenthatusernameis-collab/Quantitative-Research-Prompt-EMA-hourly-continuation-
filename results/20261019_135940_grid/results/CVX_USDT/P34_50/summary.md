# EMA Hourly Continuation — CVX/USDT P34_50

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.4128 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8280 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -8.0366 |
| sortino_ratio | -3.4023 |
| max_drawdown | 0.9863 |
| cagr | -0.8185 |
| net_avg_win | 17.5494 |
| net_avg_loss | -33.3885 |
| avg_hold_time_bars | 2.8563 |
| exposure | 0.1166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
