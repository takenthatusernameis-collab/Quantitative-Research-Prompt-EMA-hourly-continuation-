# EMA Hourly Continuation — VELO/USDT P20_55

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.9216 |
| sortino_ratio | -0.6321 |
| max_drawdown | 0.5832 |
| cagr | -0.2521 |
| net_avg_win | 53.9582 |
| net_avg_loss | -70.4204 |
| avg_hold_time_bars | 8.1601 |
| exposure | 0.1970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
