# EMA Hourly Continuation — MOODENG/USDT P12_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7643 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.2384 |
| sortino_ratio | -0.8241 |
| max_drawdown | 0.5791 |
| cagr | -0.3170 |
| net_avg_win | 66.3911 |
| net_avg_loss | -81.9379 |
| avg_hold_time_bars | 10.4234 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
