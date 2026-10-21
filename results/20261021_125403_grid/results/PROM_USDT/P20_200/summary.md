# EMA Hourly Continuation — PROM/USDT P20_200

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.6819 |
| gross_win_rate | 0.4094 |
| sharpe_ratio | -3.6875 |
| sortino_ratio | -0.9599 |
| max_drawdown | 0.6977 |
| cagr | -0.3615 |
| net_avg_win | 54.1293 |
| net_avg_loss | -69.7467 |
| avg_hold_time_bars | 38.4708 |
| exposure | 0.5980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
