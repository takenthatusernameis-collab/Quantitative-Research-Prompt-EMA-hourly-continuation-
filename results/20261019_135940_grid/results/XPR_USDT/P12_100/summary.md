# EMA Hourly Continuation — XPR/USDT P12_100

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.4763 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.7808 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -6.7342 |
| sortino_ratio | -2.6740 |
| max_drawdown | 0.9673 |
| cagr | -0.7380 |
| net_avg_win | 25.0158 |
| net_avg_loss | -39.9883 |
| avg_hold_time_bars | 12.5074 |
| exposure | 0.4616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
