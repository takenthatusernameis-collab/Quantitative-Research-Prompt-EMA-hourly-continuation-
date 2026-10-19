# EMA Hourly Continuation — DASH/USDT P20_50

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.3648 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -8.6054 |
| sortino_ratio | -3.8362 |
| max_drawdown | 0.9920 |
| cagr | -0.8537 |
| net_avg_win | 13.2462 |
| net_avg_loss | -27.0636 |
| avg_hold_time_bars | 4.7954 |
| exposure | 0.2195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
