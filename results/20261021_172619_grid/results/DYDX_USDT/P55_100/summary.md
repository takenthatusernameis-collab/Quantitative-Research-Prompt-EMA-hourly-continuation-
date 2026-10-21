# EMA Hourly Continuation — DYDX/USDT P55_100

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6983 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.0085 |
| sortino_ratio | -0.5387 |
| max_drawdown | 0.4718 |
| cagr | -0.2187 |
| net_avg_win | 62.8930 |
| net_avg_loss | -84.1288 |
| avg_hold_time_bars | 7.2614 |
| exposure | 0.1162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
