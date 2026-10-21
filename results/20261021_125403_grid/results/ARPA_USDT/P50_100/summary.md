# EMA Hourly Continuation — ARPA/USDT P50_100

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8286 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -3.5050 |
| sortino_ratio | -1.0697 |
| max_drawdown | 0.7298 |
| cagr | -0.3875 |
| net_avg_win | 47.0881 |
| net_avg_loss | -68.6763 |
| avg_hold_time_bars | 8.2723 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
