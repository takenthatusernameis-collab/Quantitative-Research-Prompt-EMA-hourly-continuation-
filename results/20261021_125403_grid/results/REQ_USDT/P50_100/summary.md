# EMA Hourly Continuation — REQ/USDT P50_100

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.5936 |
| sortino_ratio | -1.0252 |
| max_drawdown | 0.7013 |
| cagr | -0.3760 |
| net_avg_win | 59.4253 |
| net_avg_loss | -84.9959 |
| avg_hold_time_bars | 9.1035 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
