# EMA Hourly Continuation — EIGEN/USDT P34_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7559 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.9783 |
| sortino_ratio | -0.5896 |
| max_drawdown | 0.4944 |
| cagr | -0.2410 |
| net_avg_win | 76.4582 |
| net_avg_loss | -96.1954 |
| avg_hold_time_bars | 22.9554 |
| exposure | 0.4586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
