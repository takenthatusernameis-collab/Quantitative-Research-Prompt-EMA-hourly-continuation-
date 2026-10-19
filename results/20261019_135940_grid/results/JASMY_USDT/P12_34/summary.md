# EMA Hourly Continuation — JASMY/USDT P12_34

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1281 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7461 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -8.7886 |
| sortino_ratio | -4.4223 |
| max_drawdown | 0.9960 |
| cagr | -0.8884 |
| net_avg_win | 13.6884 |
| net_avg_loss | -24.8729 |
| avg_hold_time_bars | 4.0664 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
