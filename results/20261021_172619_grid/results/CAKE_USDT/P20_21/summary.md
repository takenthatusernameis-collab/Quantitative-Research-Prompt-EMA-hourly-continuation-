# EMA Hourly Continuation — CAKE/USDT P20_21

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 111 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5495 |
| gross_profit_factor | 1.2093 |
| gross_win_rate | 0.5495 |
| sharpe_ratio | -0.6832 |
| sortino_ratio | -0.1044 |
| max_drawdown | 0.1349 |
| cagr | -0.0470 |
| net_avg_win | 76.9593 |
| net_avg_loss | -116.6574 |
| avg_hold_time_bars | 6.4865 |
| exposure | 0.0327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
