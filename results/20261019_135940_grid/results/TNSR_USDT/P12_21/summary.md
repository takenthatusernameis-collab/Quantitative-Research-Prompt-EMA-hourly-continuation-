# EMA Hourly Continuation — TNSR/USDT P12_21

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1431 |
| net_profit_factor | 0.5208 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -10.4412 |
| sortino_ratio | -5.5764 |
| max_drawdown | 0.9991 |
| cagr | -0.9375 |
| net_avg_win | 17.5119 |
| net_avg_loss | -25.7068 |
| avg_hold_time_bars | 2.5283 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
