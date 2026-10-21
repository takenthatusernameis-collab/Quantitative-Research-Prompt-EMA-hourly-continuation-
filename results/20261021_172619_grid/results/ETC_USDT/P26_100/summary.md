# EMA Hourly Continuation — ETC/USDT P26_100

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9736 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.3386 |
| sortino_ratio | -0.6966 |
| max_drawdown | 0.5658 |
| cagr | -0.2730 |
| net_avg_win | 60.6951 |
| net_avg_loss | -83.8090 |
| avg_hold_time_bars | 16.2402 |
| exposure | 0.3196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
