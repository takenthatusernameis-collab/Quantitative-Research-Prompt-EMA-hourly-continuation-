# EMA Hourly Continuation — SAND/USDT P12_55

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.4993 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -6.8845 |
| sortino_ratio | -2.9446 |
| max_drawdown | 0.9753 |
| cagr | -0.7651 |
| net_avg_win | 23.5718 |
| net_avg_loss | -37.5453 |
| avg_hold_time_bars | 9.3591 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
