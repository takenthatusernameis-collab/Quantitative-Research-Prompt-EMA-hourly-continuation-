# EMA Hourly Continuation — CATI/USDT P21_26

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.2391 |
| sortino_ratio | -0.2358 |
| max_drawdown | 0.2279 |
| cagr | -0.1038 |
| net_avg_win | 81.2390 |
| net_avg_loss | -111.8412 |
| avg_hold_time_bars | 5.5479 |
| exposure | 0.0444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
