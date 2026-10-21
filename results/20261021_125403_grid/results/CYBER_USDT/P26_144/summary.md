# EMA Hourly Continuation — CYBER/USDT P26_144

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8013 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.3583 |
| sortino_ratio | -0.3839 |
| max_drawdown | 0.4056 |
| cagr | -0.1633 |
| net_avg_win | 75.0191 |
| net_avg_loss | -92.1938 |
| avg_hold_time_bars | 28.3887 |
| exposure | 0.5045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
