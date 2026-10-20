# EMA Hourly Continuation — LISTA/USDT P8_50

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.6511 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9461 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.7744 |
| sortino_ratio | -2.1043 |
| max_drawdown | 0.9108 |
| cagr | -0.6344 |
| net_avg_win | 39.0796 |
| net_avg_loss | -53.2391 |
| avg_hold_time_bars | 10.5060 |
| exposure | 0.4721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
