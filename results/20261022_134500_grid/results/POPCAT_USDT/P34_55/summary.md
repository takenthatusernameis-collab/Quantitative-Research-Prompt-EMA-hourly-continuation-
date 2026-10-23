# EMA Hourly Continuation — POPCAT/USDT P34_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 823 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.8299 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -7.2112 |
| sortino_ratio | -3.1474 |
| max_drawdown | 0.9635 |
| cagr | -0.7812 |
| net_avg_win | 32.1517 |
| net_avg_loss | -45.1200 |
| avg_hold_time_bars | 3.1033 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
