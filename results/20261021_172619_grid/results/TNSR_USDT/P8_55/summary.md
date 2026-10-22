# EMA Hourly Continuation — TNSR/USDT P8_55

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.7624 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.5233 |
| sortino_ratio | -0.9433 |
| max_drawdown | 0.6940 |
| cagr | -0.3531 |
| net_avg_win | 64.8249 |
| net_avg_loss | -77.5098 |
| avg_hold_time_bars | 14.8988 |
| exposure | 0.4666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
