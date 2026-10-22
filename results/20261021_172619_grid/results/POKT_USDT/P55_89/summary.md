# EMA Hourly Continuation — POKT/USDT P55_89

**Symbol:** POKT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6189 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -3.1970 |
| sortino_ratio | -0.8509 |
| max_drawdown | 0.6412 |
| cagr | -0.3243 |
| net_avg_win | 65.3626 |
| net_avg_loss | -83.6357 |
| avg_hold_time_bars | 9.1388 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
