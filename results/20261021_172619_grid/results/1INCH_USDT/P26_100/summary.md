# EMA Hourly Continuation — 1INCH/USDT P26_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6623 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.9115 |
| sortino_ratio | -0.9090 |
| max_drawdown | 0.6602 |
| cagr | -0.3416 |
| net_avg_win | 57.1529 |
| net_avg_loss | -74.8808 |
| avg_hold_time_bars | 16.7271 |
| exposure | 0.3650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
