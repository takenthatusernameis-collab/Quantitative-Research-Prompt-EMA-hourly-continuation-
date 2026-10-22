# EMA Hourly Continuation — BIGTIME/USDT P8_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7966 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.8642 |
| sortino_ratio | -0.6577 |
| max_drawdown | 0.5560 |
| cagr | -0.2625 |
| net_avg_win | 69.3162 |
| net_avg_loss | -85.3209 |
| avg_hold_time_bars | 19.0163 |
| exposure | 0.5267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
