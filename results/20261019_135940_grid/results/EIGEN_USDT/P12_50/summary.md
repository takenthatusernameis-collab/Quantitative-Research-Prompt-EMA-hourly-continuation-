# EMA Hourly Continuation — EIGEN/USDT P12_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -4.8507 |
| sortino_ratio | -2.2102 |
| max_drawdown | 0.8879 |
| cagr | -0.6517 |
| net_avg_win | 35.6596 |
| net_avg_loss | -52.3120 |
| avg_hold_time_bars | 7.1785 |
| exposure | 0.3423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
