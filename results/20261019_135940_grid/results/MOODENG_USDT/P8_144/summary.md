# EMA Hourly Continuation — MOODENG/USDT P8_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.9256 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1790 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | -0.4809 |
| sortino_ratio | -0.1392 |
| max_drawdown | 0.2849 |
| cagr | -0.0674 |
| net_avg_win | 92.7109 |
| net_avg_loss | -116.3171 |
| avg_hold_time_bars | 41.8299 |
| exposure | 0.7754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
