# EMA Hourly Continuation — EWT/USDT P21_100

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.4445 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.6908 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -6.2962 |
| sortino_ratio | -2.3341 |
| max_drawdown | 0.9461 |
| cagr | -0.6822 |
| net_avg_win | 26.4102 |
| net_avg_loss | -40.6487 |
| avg_hold_time_bars | 10.6960 |
| exposure | 0.3423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
