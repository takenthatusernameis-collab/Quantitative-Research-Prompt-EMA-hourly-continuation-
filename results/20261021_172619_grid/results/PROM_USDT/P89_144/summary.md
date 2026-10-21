# EMA Hourly Continuation — PROM/USDT P89_144

**Symbol:** PROM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.4720 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7077 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -3.6240 |
| sortino_ratio | -0.8955 |
| max_drawdown | 0.6610 |
| cagr | -0.3409 |
| net_avg_win | 44.6363 |
| net_avg_loss | -71.0561 |
| avg_hold_time_bars | 8.4422 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
