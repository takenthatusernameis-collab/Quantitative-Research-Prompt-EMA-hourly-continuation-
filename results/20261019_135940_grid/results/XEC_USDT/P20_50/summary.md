# EMA Hourly Continuation — XEC/USDT P20_50

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.4815 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.2262 |
| sortino_ratio | -3.7660 |
| max_drawdown | 0.9905 |
| cagr | -0.8420 |
| net_avg_win | 19.7771 |
| net_avg_loss | -32.8199 |
| avg_hold_time_bars | 5.4499 |
| exposure | 0.2582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
