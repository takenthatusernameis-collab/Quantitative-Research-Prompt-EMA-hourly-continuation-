# EMA Hourly Continuation — OSMO/USDT P21_100

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8521 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0898 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -1.1404 |
| sortino_ratio | -0.3517 |
| max_drawdown | 0.4257 |
| cagr | -0.1516 |
| net_avg_win | 81.5896 |
| net_avg_loss | -103.5441 |
| avg_hold_time_bars | 20.6674 |
| exposure | 0.4321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
