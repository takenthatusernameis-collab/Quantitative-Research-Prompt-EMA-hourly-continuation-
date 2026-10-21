# EMA Hourly Continuation — CTC/USDT P34_55

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.5197 |
| sortino_ratio | -0.6689 |
| max_drawdown | 0.5614 |
| cagr | -0.2646 |
| net_avg_win | 56.4027 |
| net_avg_loss | -86.1894 |
| avg_hold_time_bars | 6.6871 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
