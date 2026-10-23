# EMA Hourly Continuation — LUNA/USDT P26_100

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.4845 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -6.7995 |
| sortino_ratio | -2.6267 |
| max_drawdown | 0.9641 |
| cagr | -0.7316 |
| net_avg_win | 27.5206 |
| net_avg_loss | -43.3567 |
| avg_hold_time_bars | 9.2263 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
