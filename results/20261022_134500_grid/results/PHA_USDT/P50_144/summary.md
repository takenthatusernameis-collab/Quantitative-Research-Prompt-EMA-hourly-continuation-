# EMA Hourly Continuation — PHA/USDT P50_144

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -4.0883 |
| sortino_ratio | -1.3079 |
| max_drawdown | 0.8056 |
| cagr | -0.4662 |
| net_avg_win | 42.5995 |
| net_avg_loss | -61.0760 |
| avg_hold_time_bars | 10.6820 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
