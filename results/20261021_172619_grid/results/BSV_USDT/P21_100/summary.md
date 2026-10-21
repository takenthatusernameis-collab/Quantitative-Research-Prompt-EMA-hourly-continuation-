# EMA Hourly Continuation — BSV/USDT P21_100

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.6323 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -3.4744 |
| sortino_ratio | -1.0917 |
| max_drawdown | 0.7255 |
| cagr | -0.3948 |
| net_avg_win | 56.5369 |
| net_avg_loss | -71.4002 |
| avg_hold_time_bars | 18.8228 |
| exposure | 0.4201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
