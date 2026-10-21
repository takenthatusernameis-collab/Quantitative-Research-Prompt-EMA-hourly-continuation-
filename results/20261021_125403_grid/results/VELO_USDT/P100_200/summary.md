# EMA Hourly Continuation — VELO/USDT P100_200

**Symbol:** VELO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.9100 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.0962 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.4409 |
| sortino_ratio | -0.1056 |
| max_drawdown | 0.1629 |
| cagr | -0.0504 |
| net_avg_win | 84.9833 |
| net_avg_loss | -103.3689 |
| avg_hold_time_bars | 11.0362 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
