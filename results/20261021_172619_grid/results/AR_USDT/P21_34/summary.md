# EMA Hourly Continuation — AR/USDT P21_34

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6242 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -2.4503 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.4999 |
| cagr | -0.2383 |
| net_avg_win | 61.8479 |
| net_avg_loss | -84.4729 |
| avg_hold_time_bars | 5.5606 |
| exposure | 0.0730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
