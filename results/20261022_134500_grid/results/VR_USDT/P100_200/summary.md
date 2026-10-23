# EMA Hourly Continuation — VR/USDT P100_200

**Symbol:** VR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.3744 |
| net_win_rate | 0.2735 |
| gross_profit_factor | 0.5751 |
| gross_win_rate | 0.2794 |
| sharpe_ratio | -10.2388 |
| sortino_ratio | -3.2837 |
| max_drawdown | 0.9907 |
| cagr | -0.8441 |
| net_avg_win | 43.2778 |
| net_avg_loss | -43.5031 |
| avg_hold_time_bars | 7.4391 |
| exposure | 0.1694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
