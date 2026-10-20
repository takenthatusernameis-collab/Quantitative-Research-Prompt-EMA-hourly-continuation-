# EMA Hourly Continuation — CETUS/USDT P8_100

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.7605 |
| sortino_ratio | -0.9545 |
| max_drawdown | 0.6989 |
| cagr | -0.3624 |
| net_avg_win | 61.4316 |
| net_avg_loss | -80.6615 |
| avg_hold_time_bars | 25.8588 |
| exposure | 0.6963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
