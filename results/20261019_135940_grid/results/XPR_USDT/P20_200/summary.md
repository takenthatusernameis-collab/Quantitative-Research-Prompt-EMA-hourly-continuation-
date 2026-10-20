# EMA Hourly Continuation — XPR/USDT P20_200

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.5945 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.0098 |
| sortino_ratio | -0.8482 |
| max_drawdown | 0.6517 |
| cagr | -0.3356 |
| net_avg_win | 49.5267 |
| net_avg_loss | -73.6191 |
| avg_hold_time_bars | 31.9901 |
| exposure | 0.5889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
