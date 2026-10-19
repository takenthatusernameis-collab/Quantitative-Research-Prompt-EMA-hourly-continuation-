# EMA Hourly Continuation — SUN/USDT P20_100

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.3919 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.7848 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -7.9078 |
| sortino_ratio | -2.7182 |
| max_drawdown | 0.9712 |
| cagr | -0.7534 |
| net_avg_win | 27.0862 |
| net_avg_loss | -43.4997 |
| avg_hold_time_bars | 16.7860 |
| exposure | 0.4542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
