# EMA Hourly Continuation — KAVA/USDT P12_200

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.7863 |
| sortino_ratio | -0.4714 |
| max_drawdown | 0.4412 |
| cagr | -0.1962 |
| net_avg_win | 69.7391 |
| net_avg_loss | -90.1596 |
| avg_hold_time_bars | 47.4927 |
| exposure | 0.7405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
