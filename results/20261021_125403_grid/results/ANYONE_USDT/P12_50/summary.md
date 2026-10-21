# EMA Hourly Continuation — ANYONE/USDT P12_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8532 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -2.5879 |
| sortino_ratio | -0.9307 |
| max_drawdown | 0.6298 |
| cagr | -0.3497 |
| net_avg_win | 61.1257 |
| net_avg_loss | -72.4682 |
| avg_hold_time_bars | 10.9446 |
| exposure | 0.3197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
