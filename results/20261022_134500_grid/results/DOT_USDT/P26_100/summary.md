# EMA Hourly Continuation — DOT/USDT P26_100

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6371 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -3.7411 |
| sortino_ratio | -1.2964 |
| max_drawdown | 0.8044 |
| cagr | -0.4672 |
| net_avg_win | 46.4780 |
| net_avg_loss | -70.6009 |
| avg_hold_time_bars | 13.1311 |
| exposure | 0.3641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
