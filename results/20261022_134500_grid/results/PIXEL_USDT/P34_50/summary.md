# EMA Hourly Continuation — PIXEL/USDT P34_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5247 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 1.0752 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -6.8028 |
| sortino_ratio | -2.8754 |
| max_drawdown | 0.9741 |
| cagr | -0.7583 |
| net_avg_win | 25.6742 |
| net_avg_loss | -42.5231 |
| avg_hold_time_bars | 3.1902 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
