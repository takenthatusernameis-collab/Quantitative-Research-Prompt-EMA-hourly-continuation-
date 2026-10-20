# EMA Hourly Continuation — MOODENG/USDT P21_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6513 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -3.9474 |
| sortino_ratio | -1.4355 |
| max_drawdown | 0.7659 |
| cagr | -0.4994 |
| net_avg_win | 56.3375 |
| net_avg_loss | -71.7023 |
| avg_hold_time_bars | 13.5144 |
| exposure | 0.4158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
