# EMA Hourly Continuation — BAND/USDT P12_50

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 1.0730 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -4.9866 |
| sortino_ratio | -2.1153 |
| max_drawdown | 0.9257 |
| cagr | -0.6390 |
| net_avg_win | 39.0012 |
| net_avg_loss | -55.8046 |
| avg_hold_time_bars | 9.0997 |
| exposure | 0.3759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
