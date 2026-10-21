# EMA Hourly Continuation — STRK/USDT P12_21

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7684 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.3616 |
| sortino_ratio | -0.3339 |
| max_drawdown | 0.3450 |
| cagr | -0.1423 |
| net_avg_win | 71.7188 |
| net_avg_loss | -96.5953 |
| avg_hold_time_bars | 4.6048 |
| exposure | 0.0609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
