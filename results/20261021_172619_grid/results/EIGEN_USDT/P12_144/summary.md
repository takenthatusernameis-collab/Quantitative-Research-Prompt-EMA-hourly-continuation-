# EMA Hourly Continuation — EIGEN/USDT P12_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -0.8772 |
| sortino_ratio | -0.2334 |
| max_drawdown | 0.2920 |
| cagr | -0.1042 |
| net_avg_win | 89.4710 |
| net_avg_loss | -101.7218 |
| avg_hold_time_bars | 42.5371 |
| exposure | 0.6699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
