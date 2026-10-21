# EMA Hourly Continuation — AURORA/USDT P21_50

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.5496 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8014 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -3.9171 |
| sortino_ratio | -1.1619 |
| max_drawdown | 0.7583 |
| cagr | -0.4168 |
| net_avg_win | 46.6614 |
| net_avg_loss | -68.9132 |
| avg_hold_time_bars | 10.3256 |
| exposure | 0.2032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
