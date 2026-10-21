# EMA Hourly Continuation — EGLD/USDT P21_55

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.6437 |
| sortino_ratio | -0.8883 |
| max_drawdown | 0.6623 |
| cagr | -0.3343 |
| net_avg_win | 56.6536 |
| net_avg_loss | -77.0148 |
| avg_hold_time_bars | 8.3382 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
