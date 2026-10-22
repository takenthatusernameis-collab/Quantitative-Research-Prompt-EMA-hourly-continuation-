# EMA Hourly Continuation — EIGEN/USDT P21_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -8.4671 |
| sortino_ratio | -3.9732 |
| max_drawdown | 0.9839 |
| cagr | -0.8623 |
| net_avg_win | 20.4724 |
| net_avg_loss | -34.7198 |
| avg_hold_time_bars | 2.6235 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
