# EMA Hourly Continuation — COMP/USDT P12_50

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.4520 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -7.3391 |
| sortino_ratio | -3.4648 |
| max_drawdown | 0.9856 |
| cagr | -0.8148 |
| net_avg_win | 15.7841 |
| net_avg_loss | -29.5791 |
| avg_hold_time_bars | 7.4844 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
