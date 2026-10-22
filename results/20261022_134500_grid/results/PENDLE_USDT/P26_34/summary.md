# EMA Hourly Continuation — PENDLE/USDT P26_34

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.3291 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.7193 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -10.7066 |
| sortino_ratio | -5.1183 |
| max_drawdown | 0.9985 |
| cagr | -0.9242 |
| net_avg_win | 10.6453 |
| net_avg_loss | -22.5819 |
| avg_hold_time_bars | 2.2395 |
| exposure | 0.1139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
