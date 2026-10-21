# EMA Hourly Continuation — DOT/USDT P34_100

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8328 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0760 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -1.1221 |
| sortino_ratio | -0.3292 |
| max_drawdown | 0.3555 |
| cagr | -0.1420 |
| net_avg_win | 73.6578 |
| net_avg_loss | -95.9978 |
| avg_hold_time_bars | 13.7253 |
| exposure | 0.2589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
