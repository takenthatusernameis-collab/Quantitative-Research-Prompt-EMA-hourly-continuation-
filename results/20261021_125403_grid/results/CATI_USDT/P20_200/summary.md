# EMA Hourly Continuation — CATI/USDT P20_200

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.7414 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -2.6589 |
| sortino_ratio | -0.6378 |
| max_drawdown | 0.5090 |
| cagr | -0.2555 |
| net_avg_win | 68.8024 |
| net_avg_loss | -85.2356 |
| avg_hold_time_bars | 50.5417 |
| exposure | 0.6649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
