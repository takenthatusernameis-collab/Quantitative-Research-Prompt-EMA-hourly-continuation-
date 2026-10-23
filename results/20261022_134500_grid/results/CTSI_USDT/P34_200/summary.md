# EMA Hourly Continuation — CTSI/USDT P34_200

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -3.5962 |
| sortino_ratio | -1.0396 |
| max_drawdown | 0.7071 |
| cagr | -0.3835 |
| net_avg_win | 59.7198 |
| net_avg_loss | -75.5977 |
| avg_hold_time_bars | 28.7890 |
| exposure | 0.5457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
