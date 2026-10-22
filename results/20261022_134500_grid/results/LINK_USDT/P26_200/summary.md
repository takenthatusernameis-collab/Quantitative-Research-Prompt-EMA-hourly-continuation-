# EMA Hourly Continuation — LINK/USDT P26_200

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.1190 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -2.2110 |
| sortino_ratio | -0.6154 |
| max_drawdown | 0.5521 |
| cagr | -0.2582 |
| net_avg_win | 59.4131 |
| net_avg_loss | -91.0856 |
| avg_hold_time_bars | 28.7215 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
