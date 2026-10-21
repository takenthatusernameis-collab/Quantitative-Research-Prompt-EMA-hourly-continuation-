# EMA Hourly Continuation — EIGEN/USDT P8_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6551 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.0528 |
| sortino_ratio | -1.0193 |
| max_drawdown | 0.6336 |
| cagr | -0.3745 |
| net_avg_win | 57.2793 |
| net_avg_loss | -72.8587 |
| avg_hold_time_bars | 5.0909 |
| exposure | 0.1278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
