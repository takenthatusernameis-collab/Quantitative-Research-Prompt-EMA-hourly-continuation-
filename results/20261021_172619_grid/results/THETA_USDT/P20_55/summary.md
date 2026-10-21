# EMA Hourly Continuation — THETA/USDT P20_55

**Symbol:** THETA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7494 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -1.9523 |
| sortino_ratio | -0.6171 |
| max_drawdown | 0.5394 |
| cagr | -0.2463 |
| net_avg_win | 63.0713 |
| net_avg_loss | -82.7932 |
| avg_hold_time_bars | 8.7407 |
| exposure | 0.1931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
