# EMA Hourly Continuation — CTC/USDT P21_50

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0497 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -2.2155 |
| sortino_ratio | -0.7333 |
| max_drawdown | 0.5889 |
| cagr | -0.2858 |
| net_avg_win | 56.8871 |
| net_avg_loss | -82.0889 |
| avg_hold_time_bars | 8.4340 |
| exposure | 0.2032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
