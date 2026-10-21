# EMA Hourly Continuation — CKB/USDT P89_100

**Symbol:** CKB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.9256 |
| net_win_rate | 0.5870 |
| gross_profit_factor | 1.4051 |
| gross_win_rate | 0.5870 |
| sharpe_ratio | -0.2469 |
| sortino_ratio | -0.0425 |
| max_drawdown | 0.1419 |
| cagr | -0.0208 |
| net_avg_win | 79.0415 |
| net_avg_loss | -121.3478 |
| avg_hold_time_bars | 4.7609 |
| exposure | 0.0299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
