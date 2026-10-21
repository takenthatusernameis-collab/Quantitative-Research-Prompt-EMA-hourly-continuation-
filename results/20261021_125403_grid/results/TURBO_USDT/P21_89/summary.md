# EMA Hourly Continuation — TURBO/USDT P21_89

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7554 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9176 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.0765 |
| sortino_ratio | -0.6660 |
| max_drawdown | 0.5421 |
| cagr | -0.2646 |
| net_avg_win | 72.1714 |
| net_avg_loss | -88.1546 |
| avg_hold_time_bars | 14.7565 |
| exposure | 0.3405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
