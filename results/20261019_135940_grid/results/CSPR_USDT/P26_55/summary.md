# EMA Hourly Continuation — CSPR/USDT P26_55

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.3519 |
| net_win_rate | 0.3895 |
| gross_profit_factor | 0.7320 |
| gross_win_rate | 0.4084 |
| sharpe_ratio | -10.8083 |
| sortino_ratio | -5.3163 |
| max_drawdown | 0.9989 |
| cagr | -0.9328 |
| net_avg_win | 11.4399 |
| net_avg_loss | -20.7418 |
| avg_hold_time_bars | 3.3106 |
| exposure | 0.1831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
