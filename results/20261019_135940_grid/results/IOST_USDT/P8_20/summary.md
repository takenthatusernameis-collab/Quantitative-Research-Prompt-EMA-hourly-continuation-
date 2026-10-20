# EMA Hourly Continuation — IOST/USDT P8_20

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1581 |
| net_profit_factor | 0.3612 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.9375 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -11.6558 |
| sortino_ratio | -6.5705 |
| max_drawdown | 0.9998 |
| cagr | -0.9638 |
| net_avg_win | 8.1590 |
| net_avg_loss | -17.6259 |
| avg_hold_time_bars | 3.4845 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
