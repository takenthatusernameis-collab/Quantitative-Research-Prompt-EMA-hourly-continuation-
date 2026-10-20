# EMA Hourly Continuation — ZIL/USDT P20_100

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -4.7477 |
| sortino_ratio | -1.7571 |
| max_drawdown | 0.8907 |
| cagr | -0.5716 |
| net_avg_win | 39.9783 |
| net_avg_loss | -59.1923 |
| avg_hold_time_bars | 12.9029 |
| exposure | 0.4047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
