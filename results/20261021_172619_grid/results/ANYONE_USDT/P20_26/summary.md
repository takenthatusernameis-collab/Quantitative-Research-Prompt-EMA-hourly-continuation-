# EMA Hourly Continuation — ANYONE/USDT P20_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.7092 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9266 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -1.7563 |
| sortino_ratio | -0.4001 |
| max_drawdown | 0.4248 |
| cagr | -0.1687 |
| net_avg_win | 74.9451 |
| net_avg_loss | -98.5759 |
| avg_hold_time_bars | 5.0522 |
| exposure | 0.0587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
