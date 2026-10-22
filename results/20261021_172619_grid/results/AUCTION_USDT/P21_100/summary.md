# EMA Hourly Continuation — AUCTION/USDT P21_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6329 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8452 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.4810 |
| sortino_ratio | -1.1265 |
| max_drawdown | 0.7467 |
| cagr | -0.4098 |
| net_avg_win | 53.0641 |
| net_avg_loss | -69.8157 |
| avg_hold_time_bars | 17.3118 |
| exposure | 0.4121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
