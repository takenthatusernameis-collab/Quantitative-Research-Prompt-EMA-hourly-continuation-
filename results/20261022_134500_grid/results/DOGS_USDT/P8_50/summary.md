# EMA Hourly Continuation — DOGS/USDT P8_50

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.6279 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -5.3642 |
| sortino_ratio | -2.5485 |
| max_drawdown | 0.9273 |
| cagr | -0.7024 |
| net_avg_win | 33.9838 |
| net_avg_loss | -48.7197 |
| avg_hold_time_bars | 8.8980 |
| exposure | 0.4584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
