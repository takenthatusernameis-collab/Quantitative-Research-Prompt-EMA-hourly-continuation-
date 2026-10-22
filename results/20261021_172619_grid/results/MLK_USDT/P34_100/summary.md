# EMA Hourly Continuation — MLK/USDT P34_100

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.3874 |
| net_win_rate | 0.3325 |
| gross_profit_factor | 0.5359 |
| gross_win_rate | 0.3325 |
| sharpe_ratio | -6.1497 |
| sortino_ratio | -1.7549 |
| max_drawdown | 0.8768 |
| cagr | -0.5607 |
| net_avg_win | 40.6581 |
| net_avg_loss | -52.2845 |
| avg_hold_time_bars | 12.3178 |
| exposure | 0.2280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
