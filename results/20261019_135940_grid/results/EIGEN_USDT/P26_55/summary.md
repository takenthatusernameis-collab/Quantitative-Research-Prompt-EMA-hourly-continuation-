# EMA Hourly Continuation — EIGEN/USDT P26_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8455 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -5.4592 |
| sortino_ratio | -2.3484 |
| max_drawdown | 0.9028 |
| cagr | -0.6776 |
| net_avg_win | 30.6286 |
| net_avg_loss | -49.2221 |
| avg_hold_time_bars | 3.8521 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
