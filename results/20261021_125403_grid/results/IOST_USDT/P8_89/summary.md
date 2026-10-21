# EMA Hourly Continuation — IOST/USDT P8_89

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.9180 |
| net_win_rate | 0.5425 |
| gross_profit_factor | 1.1860 |
| gross_win_rate | 0.5444 |
| sharpe_ratio | -0.5765 |
| sortino_ratio | -0.1898 |
| max_drawdown | 0.3329 |
| cagr | -0.0893 |
| net_avg_win | 83.3562 |
| net_avg_loss | -107.6623 |
| avg_hold_time_bars | 27.8359 |
| exposure | 0.6554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
