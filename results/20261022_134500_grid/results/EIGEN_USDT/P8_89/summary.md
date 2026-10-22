# EMA Hourly Continuation — EIGEN/USDT P8_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -2.8223 |
| sortino_ratio | -1.0327 |
| max_drawdown | 0.6657 |
| cagr | -0.3874 |
| net_avg_win | 60.6001 |
| net_avg_loss | -80.2920 |
| avg_hold_time_bars | 21.2396 |
| exposure | 0.6512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
