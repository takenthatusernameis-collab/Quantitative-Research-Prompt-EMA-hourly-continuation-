# EMA Hourly Continuation — HBAR/USDT P8_200

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8953 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0813 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.5839 |
| sortino_ratio | -0.1477 |
| max_drawdown | 0.3056 |
| cagr | -0.0689 |
| net_avg_win | 86.5635 |
| net_avg_loss | -105.8361 |
| avg_hold_time_bars | 55.8097 |
| exposure | 0.7864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
