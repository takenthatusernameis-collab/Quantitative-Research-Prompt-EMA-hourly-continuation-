# EMA Hourly Continuation — EGLD/USDT P20_55

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.4636 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8806 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -7.1544 |
| sortino_ratio | -3.1399 |
| max_drawdown | 0.9799 |
| cagr | -0.7867 |
| net_avg_win | 19.1962 |
| net_avg_loss | -34.2572 |
| avg_hold_time_bars | 5.5637 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
