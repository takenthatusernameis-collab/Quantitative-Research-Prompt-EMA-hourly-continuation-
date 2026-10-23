# EMA Hourly Continuation — CWEB/USDT P12_100

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.1191 |
| sortino_ratio | -1.2707 |
| max_drawdown | 0.7995 |
| cagr | -0.4691 |
| net_avg_win | 51.0722 |
| net_avg_loss | -71.2901 |
| avg_hold_time_bars | 28.1263 |
| exposure | 0.6277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
