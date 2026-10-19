# EMA Hourly Continuation — SUN/USDT P8_50

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.3394 |
| net_win_rate | 0.3994 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -9.9984 |
| sortino_ratio | -4.3229 |
| max_drawdown | 0.9964 |
| cagr | -0.8920 |
| net_avg_win | 13.7234 |
| net_avg_loss | -26.8848 |
| avg_hold_time_bars | 11.8319 |
| exposure | 0.5001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
