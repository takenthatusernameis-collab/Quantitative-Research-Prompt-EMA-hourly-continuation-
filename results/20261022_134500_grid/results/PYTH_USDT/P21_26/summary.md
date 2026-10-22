# EMA Hourly Continuation — PYTH/USDT P21_26

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.2794 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.7420 |
| gross_win_rate | 0.4149 |
| sharpe_ratio | -12.8954 |
| sortino_ratio | -6.2795 |
| max_drawdown | 0.9998 |
| cagr | -0.9645 |
| net_avg_win | 8.8121 |
| net_avg_loss | -19.4874 |
| avg_hold_time_bars | 1.7552 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
