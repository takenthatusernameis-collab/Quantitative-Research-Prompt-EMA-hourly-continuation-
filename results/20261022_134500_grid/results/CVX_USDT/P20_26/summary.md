# EMA Hourly Continuation — CVX/USDT P20_26

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.2472 |
| net_win_rate | 0.3827 |
| gross_profit_factor | 0.6741 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -12.9220 |
| sortino_ratio | -6.4429 |
| max_drawdown | 0.9998 |
| cagr | -0.9651 |
| net_avg_win | 7.1359 |
| net_avg_loss | -17.8980 |
| avg_hold_time_bars | 2.1098 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
