# EMA Hourly Continuation — MOODENG/USDT P26_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8344 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9736 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -1.0920 |
| sortino_ratio | -0.2931 |
| max_drawdown | 0.3083 |
| cagr | -0.1284 |
| net_avg_win | 86.9734 |
| net_avg_loss | -101.4023 |
| avg_hold_time_bars | 32.4241 |
| exposure | 0.5203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
