# EMA Hourly Continuation — ETN/USDT P34_100

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6166 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -3.0284 |
| sortino_ratio | -0.8660 |
| max_drawdown | 0.5798 |
| cagr | -0.3302 |
| net_avg_win | 61.0525 |
| net_avg_loss | -77.7541 |
| avg_hold_time_bars | 12.4223 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
