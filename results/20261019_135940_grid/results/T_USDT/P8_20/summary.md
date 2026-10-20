# EMA Hourly Continuation — T/USDT P8_20

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.4621 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -9.6820 |
| sortino_ratio | -4.8109 |
| max_drawdown | 0.9976 |
| cagr | -0.9075 |
| net_avg_win | 15.8111 |
| net_avg_loss | -26.8378 |
| avg_hold_time_bars | 4.5434 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
