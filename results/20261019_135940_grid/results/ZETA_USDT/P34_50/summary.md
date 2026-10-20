# EMA Hourly Continuation — ZETA/USDT P34_50

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.4063 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.8145 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -9.1177 |
| sortino_ratio | -3.9775 |
| max_drawdown | 0.9934 |
| cagr | -0.8626 |
| net_avg_win | 17.0392 |
| net_avg_loss | -30.4213 |
| avg_hold_time_bars | 2.9874 |
| exposure | 0.1283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
