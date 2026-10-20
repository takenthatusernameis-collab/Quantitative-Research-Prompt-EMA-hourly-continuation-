# EMA Hourly Continuation — DUSK/USDT P55_100

**Symbol:** DUSK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5607 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.4662 |
| sortino_ratio | -1.5921 |
| max_drawdown | 0.8600 |
| cagr | -0.5399 |
| net_avg_win | 35.8848 |
| net_avg_loss | -56.7485 |
| avg_hold_time_bars | 5.2296 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
