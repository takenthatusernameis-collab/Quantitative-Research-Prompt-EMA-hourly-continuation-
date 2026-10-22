# EMA Hourly Continuation — ATOM/USDT P20_200

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7309 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -1.7718 |
| sortino_ratio | -0.4840 |
| max_drawdown | 0.4719 |
| cagr | -0.2042 |
| net_avg_win | 62.7563 |
| net_avg_loss | -89.1587 |
| avg_hold_time_bars | 36.8059 |
| exposure | 0.6207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
