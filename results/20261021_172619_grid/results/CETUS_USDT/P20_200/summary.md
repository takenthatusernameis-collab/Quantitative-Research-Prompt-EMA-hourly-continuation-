# EMA Hourly Continuation — CETUS/USDT P20_200

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 1.1056 |
| net_win_rate | 0.5605 |
| gross_profit_factor | 1.2656 |
| gross_win_rate | 0.5605 |
| sharpe_ratio | 0.5584 |
| sortino_ratio | 0.1280 |
| max_drawdown | 0.1424 |
| cagr | 0.0518 |
| net_avg_win | 102.2888 |
| net_avg_loss | -117.9867 |
| avg_hold_time_bars | 61.8387 |
| exposure | 0.6940 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
