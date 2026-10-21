# EMA Hourly Continuation — EIGEN/USDT P20_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7291 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.2580 |
| sortino_ratio | -0.7283 |
| max_drawdown | 0.5045 |
| cagr | -0.2855 |
| net_avg_win | 68.0557 |
| net_avg_loss | -82.4629 |
| avg_hold_time_bars | 8.5286 |
| exposure | 0.1993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
