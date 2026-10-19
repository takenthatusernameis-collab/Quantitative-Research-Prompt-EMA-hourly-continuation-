# EMA Hourly Continuation — OP/USDT P21_50

**Symbol:** OP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.4910 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -6.4929 |
| sortino_ratio | -2.8313 |
| max_drawdown | 0.9704 |
| cagr | -0.7500 |
| net_avg_win | 20.6868 |
| net_avg_loss | -37.4859 |
| avg_hold_time_bars | 4.6875 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
