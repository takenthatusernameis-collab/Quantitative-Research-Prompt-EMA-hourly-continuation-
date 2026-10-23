# EMA Hourly Continuation — DEXE/USDT P50_89

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.4436 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.7733 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -5.1691 |
| sortino_ratio | -1.7081 |
| max_drawdown | 0.8848 |
| cagr | -0.5694 |
| net_avg_win | 27.9342 |
| net_avg_loss | -51.6544 |
| avg_hold_time_bars | 12.3411 |
| exposure | 0.3125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
