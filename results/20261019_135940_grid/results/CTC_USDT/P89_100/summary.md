# EMA Hourly Continuation — CTC/USDT P89_100

**Symbol:** CTC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.2331 |
| net_win_rate | 0.3498 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -10.6495 |
| sortino_ratio | -3.9045 |
| max_drawdown | 0.9953 |
| cagr | -0.8801 |
| net_avg_win | 13.7485 |
| net_avg_loss | -31.7263 |
| avg_hold_time_bars | 2.1781 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
