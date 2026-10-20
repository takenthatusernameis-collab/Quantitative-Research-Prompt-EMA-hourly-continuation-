# EMA Hourly Continuation — NOT/USDT P34_100

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -4.4918 |
| sortino_ratio | -1.6243 |
| max_drawdown | 0.8612 |
| cagr | -0.5446 |
| net_avg_win | 43.7214 |
| net_avg_loss | -63.2685 |
| avg_hold_time_bars | 9.6963 |
| exposure | 0.2924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
