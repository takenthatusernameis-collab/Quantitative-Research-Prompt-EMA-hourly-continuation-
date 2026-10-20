# EMA Hourly Continuation — CATI/USDT P8_26

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.4414 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.7212 |
| gross_win_rate | 0.4219 |
| sharpe_ratio | -12.1271 |
| sortino_ratio | -6.7619 |
| max_drawdown | 0.9992 |
| cagr | -0.9673 |
| net_avg_win | 15.1831 |
| net_avg_loss | -22.9617 |
| avg_hold_time_bars | 3.9238 |
| exposure | 0.2794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
