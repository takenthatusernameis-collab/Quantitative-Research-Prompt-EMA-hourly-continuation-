# EMA Hourly Continuation — DODO/USDT P21_50

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6756 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9078 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -3.1243 |
| sortino_ratio | -1.0616 |
| max_drawdown | 0.7166 |
| cagr | -0.3851 |
| net_avg_win | 54.9328 |
| net_avg_loss | -72.3920 |
| avg_hold_time_bars | 7.2970 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
