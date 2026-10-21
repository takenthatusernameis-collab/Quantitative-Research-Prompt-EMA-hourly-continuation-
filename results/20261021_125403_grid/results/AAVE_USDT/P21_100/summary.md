# EMA Hourly Continuation — AAVE/USDT P21_100

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8322 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0174 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -1.1425 |
| sortino_ratio | -0.3330 |
| max_drawdown | 0.3840 |
| cagr | -0.1436 |
| net_avg_win | 76.5191 |
| net_avg_loss | -94.2058 |
| avg_hold_time_bars | 20.2542 |
| exposure | 0.3802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
