# EMA Hourly Continuation — ORCA/USDT P21_89

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5931 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9081 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -3.9889 |
| sortino_ratio | -1.4386 |
| max_drawdown | 0.8425 |
| cagr | -0.5004 |
| net_avg_win | 38.5396 |
| net_avg_loss | -58.2585 |
| avg_hold_time_bars | 12.9818 |
| exposure | 0.3895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
