# EMA Hourly Continuation — EGLD/USDT P20_100

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8110 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -1.4454 |
| sortino_ratio | -0.4558 |
| max_drawdown | 0.4823 |
| cagr | -0.1905 |
| net_avg_win | 72.1328 |
| net_avg_loss | -91.5613 |
| avg_hold_time_bars | 19.1884 |
| exposure | 0.4213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
