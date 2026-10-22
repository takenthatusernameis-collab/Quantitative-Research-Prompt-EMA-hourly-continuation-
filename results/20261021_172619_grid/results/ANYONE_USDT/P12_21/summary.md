# EMA Hourly Continuation — ANYONE/USDT P12_21

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8513 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -2.6924 |
| sortino_ratio | -0.7535 |
| max_drawdown | 0.5857 |
| cagr | -0.2962 |
| net_avg_win | 67.0563 |
| net_avg_loss | -85.6469 |
| avg_hold_time_bars | 5.6239 |
| exposure | 0.0997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
