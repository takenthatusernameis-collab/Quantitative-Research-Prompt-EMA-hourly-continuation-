# EMA Hourly Continuation — METIS/USDT P20_50

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7190 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.5392 |
| sortino_ratio | -0.8532 |
| max_drawdown | 0.6520 |
| cagr | -0.3236 |
| net_avg_win | 59.6902 |
| net_avg_loss | -78.3455 |
| avg_hold_time_bars | 7.4420 |
| exposure | 0.1867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
