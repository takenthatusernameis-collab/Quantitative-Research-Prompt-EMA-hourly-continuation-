# EMA Hourly Continuation — MOODENG/USDT P8_12

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.4367 |
| net_win_rate | 0.3704 |
| gross_profit_factor | 0.7447 |
| gross_win_rate | 0.4199 |
| sharpe_ratio | -15.1392 |
| sortino_ratio | -9.0439 |
| max_drawdown | 0.9999 |
| cagr | -0.9907 |
| net_avg_win | 14.3825 |
| net_avg_loss | -19.3794 |
| avg_hold_time_bars | 1.9402 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
