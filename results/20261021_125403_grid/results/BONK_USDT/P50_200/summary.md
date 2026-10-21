# EMA Hourly Continuation — BONK/USDT P50_200

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.8097 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -0.9831 |
| sortino_ratio | -0.2215 |
| max_drawdown | 0.3047 |
| cagr | -0.0982 |
| net_avg_win | 79.0889 |
| net_avg_loss | -94.6024 |
| avg_hold_time_bars | 35.5760 |
| exposure | 0.4043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
