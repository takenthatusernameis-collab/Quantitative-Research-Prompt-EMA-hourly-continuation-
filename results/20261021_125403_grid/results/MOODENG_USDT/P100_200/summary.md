# EMA Hourly Continuation — MOODENG/USDT P100_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.8722 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0589 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -0.6524 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.1854 |
| cagr | -0.0687 |
| net_avg_win | 85.5509 |
| net_avg_loss | -104.8155 |
| avg_hold_time_bars | 15.9052 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
