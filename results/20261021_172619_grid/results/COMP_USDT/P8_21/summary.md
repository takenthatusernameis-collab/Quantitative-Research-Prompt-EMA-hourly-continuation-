# EMA Hourly Continuation — COMP/USDT P8_21

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5535 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8212 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -5.2091 |
| sortino_ratio | -2.0115 |
| max_drawdown | 0.9045 |
| cagr | -0.6045 |
| net_avg_win | 34.3244 |
| net_avg_loss | -50.4151 |
| avg_hold_time_bars | 5.0371 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
