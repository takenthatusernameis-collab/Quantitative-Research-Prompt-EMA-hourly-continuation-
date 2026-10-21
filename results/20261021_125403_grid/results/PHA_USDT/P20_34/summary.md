# EMA Hourly Continuation — PHA/USDT P20_34

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.8047 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0780 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -1.3746 |
| sortino_ratio | -0.3807 |
| max_drawdown | 0.4229 |
| cagr | -0.1608 |
| net_avg_win | 76.8422 |
| net_avg_loss | -101.8937 |
| avg_hold_time_bars | 5.0027 |
| exposure | 0.0841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
