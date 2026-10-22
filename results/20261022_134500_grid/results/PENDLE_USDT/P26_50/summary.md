# EMA Hourly Continuation — PENDLE/USDT P26_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.5302 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -6.3069 |
| sortino_ratio | -2.8107 |
| max_drawdown | 0.9662 |
| cagr | -0.7396 |
| net_avg_win | 23.5440 |
| net_avg_loss | -38.9397 |
| avg_hold_time_bars | 3.8174 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
