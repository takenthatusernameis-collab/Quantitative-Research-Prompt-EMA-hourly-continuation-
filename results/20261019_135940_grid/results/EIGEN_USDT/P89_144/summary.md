# EMA Hourly Continuation — EIGEN/USDT P89_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -4.2616 |
| sortino_ratio | -1.4079 |
| max_drawdown | 0.7477 |
| cagr | -0.4890 |
| net_avg_win | 48.3155 |
| net_avg_loss | -72.1226 |
| avg_hold_time_bars | 4.1906 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
