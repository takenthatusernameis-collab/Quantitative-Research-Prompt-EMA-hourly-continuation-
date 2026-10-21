# EMA Hourly Continuation — PROM/USDT P21_50

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.5459 |
| net_win_rate | 0.4309 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -4.5547 |
| sortino_ratio | -1.5263 |
| max_drawdown | 0.8318 |
| cagr | -0.5083 |
| net_avg_win | 41.6714 |
| net_avg_loss | -57.7890 |
| avg_hold_time_bars | 6.9156 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
