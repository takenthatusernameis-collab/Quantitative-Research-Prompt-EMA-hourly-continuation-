# EMA Hourly Continuation — MAGIC/USDT P8_21

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1493 |
| net_profit_factor | 0.4925 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -9.8978 |
| sortino_ratio | -5.3814 |
| max_drawdown | 0.9988 |
| cagr | -0.9297 |
| net_avg_win | 14.6859 |
| net_avg_loss | -23.6254 |
| avg_hold_time_bars | 3.9015 |
| exposure | 0.2648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
