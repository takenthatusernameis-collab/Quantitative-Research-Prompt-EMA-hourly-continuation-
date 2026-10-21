# EMA Hourly Continuation — TAIKO/USDT P26_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.7701 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.2421 |
| sortino_ratio | -0.2716 |
| max_drawdown | 0.2988 |
| cagr | -0.1178 |
| net_avg_win | 79.8835 |
| net_avg_loss | -98.2665 |
| avg_hold_time_bars | 63.8604 |
| exposure | 0.6810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
