# EMA Hourly Continuation — LINK/USDT P20_50

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6314 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -3.5089 |
| sortino_ratio | -1.0670 |
| max_drawdown | 0.7171 |
| cagr | -0.3885 |
| net_avg_win | 59.5432 |
| net_avg_loss | -76.3460 |
| avg_hold_time_bars | 8.5241 |
| exposure | 0.1767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
