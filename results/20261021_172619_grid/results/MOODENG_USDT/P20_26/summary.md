# EMA Hourly Continuation — MOODENG/USDT P20_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.4508 |
| net_win_rate | 0.3977 |
| gross_profit_factor | 0.6128 |
| gross_win_rate | 0.3977 |
| sharpe_ratio | -3.3070 |
| sortino_ratio | -0.6864 |
| max_drawdown | 0.4945 |
| cagr | -0.2720 |
| net_avg_win | 56.3489 |
| net_avg_loss | -82.5464 |
| avg_hold_time_bars | 6.4091 |
| exposure | 0.0624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
