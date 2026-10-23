# EMA Hourly Continuation — ETN/USDT P21_55

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.3320 |
| net_win_rate | 0.3458 |
| gross_profit_factor | 0.5239 |
| gross_win_rate | 0.3634 |
| sharpe_ratio | -11.2998 |
| sortino_ratio | -5.0879 |
| max_drawdown | 0.9956 |
| cagr | -0.9241 |
| net_avg_win | 16.7702 |
| net_avg_loss | -26.7076 |
| avg_hold_time_bars | 5.3728 |
| exposure | 0.2489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
