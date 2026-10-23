# EMA Hourly Continuation — TAIKO/USDT P8_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.6460 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -5.2037 |
| sortino_ratio | -2.3345 |
| max_drawdown | 0.9419 |
| cagr | -0.6788 |
| net_avg_win | 36.2092 |
| net_avg_loss | -52.4806 |
| avg_hold_time_bars | 10.5216 |
| exposure | 0.4913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
