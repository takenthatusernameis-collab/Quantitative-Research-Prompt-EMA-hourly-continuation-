# EMA Hourly Continuation — EIGEN/USDT P34_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.7284 |
| sortino_ratio | -2.4292 |
| max_drawdown | 0.9131 |
| cagr | -0.6933 |
| net_avg_win | 29.7968 |
| net_avg_loss | -50.2404 |
| avg_hold_time_bars | 3.0189 |
| exposure | 0.1241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
