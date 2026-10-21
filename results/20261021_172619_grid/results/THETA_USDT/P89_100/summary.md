# EMA Hourly Continuation — THETA/USDT P89_100

**Symbol:** THETA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.9377 |
| net_win_rate | 0.5696 |
| gross_profit_factor | 1.3086 |
| gross_win_rate | 0.5696 |
| sharpe_ratio | -0.1448 |
| sortino_ratio | -0.0188 |
| max_drawdown | 0.1030 |
| cagr | -0.0096 |
| net_avg_win | 80.0453 |
| net_avg_loss | -112.9863 |
| avg_hold_time_bars | 4.8987 |
| exposure | 0.0176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
