# EMA Hourly Continuation — MOODENG/USDT P100_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0762 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -2.6370 |
| sortino_ratio | -0.8054 |
| max_drawdown | 0.5521 |
| cagr | -0.3166 |
| net_avg_win | 60.8012 |
| net_avg_loss | -90.5489 |
| avg_hold_time_bars | 4.3097 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
