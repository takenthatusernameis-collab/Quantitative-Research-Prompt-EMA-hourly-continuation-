# EMA Hourly Continuation — ANKR/USDT P20_21

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7573 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -3.6209 |
| sortino_ratio | -0.7990 |
| max_drawdown | 0.6092 |
| cagr | -0.3085 |
| net_avg_win | 53.6198 |
| net_avg_loss | -84.8527 |
| avg_hold_time_bars | 5.3051 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
