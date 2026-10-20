# EMA Hourly Continuation — MOODENG/USDT P26_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 845 |
| net_profit_factor | 0.5465 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8355 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.7892 |
| sortino_ratio | -3.0750 |
| max_drawdown | 0.9538 |
| cagr | -0.7718 |
| net_avg_win | 30.6881 |
| net_avg_loss | -44.5921 |
| avg_hold_time_bars | 3.8071 |
| exposure | 0.1780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
