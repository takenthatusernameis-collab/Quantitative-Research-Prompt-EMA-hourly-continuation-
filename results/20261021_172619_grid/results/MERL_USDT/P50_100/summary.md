# EMA Hourly Continuation — MERL/USDT P50_100

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.6259 |
| sortino_ratio | -0.4513 |
| max_drawdown | 0.4460 |
| cagr | -0.1880 |
| net_avg_win | 68.6484 |
| net_avg_loss | -85.7064 |
| avg_hold_time_bars | 9.4668 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
