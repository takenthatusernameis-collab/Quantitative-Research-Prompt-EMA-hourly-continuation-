# EMA Hourly Continuation — COMP/USDT P50_100

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.5033 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -5.0632 |
| sortino_ratio | -1.8287 |
| max_drawdown | 0.8980 |
| cagr | -0.5928 |
| net_avg_win | 28.2627 |
| net_avg_loss | -52.5502 |
| avg_hold_time_bars | 6.1536 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
