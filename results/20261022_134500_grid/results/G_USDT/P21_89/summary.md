# EMA Hourly Continuation — G/USDT P21_89

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.5450 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8436 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -4.5760 |
| sortino_ratio | -1.5947 |
| max_drawdown | 0.8189 |
| cagr | -0.5317 |
| net_avg_win | 40.6389 |
| net_avg_loss | -60.9809 |
| avg_hold_time_bars | 16.2552 |
| exposure | 0.4522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
