# EMA Hourly Continuation — CHR/USDT P21_100

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6102 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -4.3259 |
| sortino_ratio | -1.5891 |
| max_drawdown | 0.8617 |
| cagr | -0.5306 |
| net_avg_win | 42.7215 |
| net_avg_loss | -58.4093 |
| avg_hold_time_bars | 13.3397 |
| exposure | 0.4141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
