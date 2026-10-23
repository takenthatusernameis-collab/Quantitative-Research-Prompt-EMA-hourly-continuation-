# EMA Hourly Continuation — LUNA/USDT P8_50

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1281 |
| net_profit_factor | 0.4984 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -9.2830 |
| sortino_ratio | -4.6858 |
| max_drawdown | 0.9969 |
| cagr | -0.8993 |
| net_avg_win | 18.2729 |
| net_avg_loss | -26.8912 |
| avg_hold_time_bars | 7.5839 |
| exposure | 0.4416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
