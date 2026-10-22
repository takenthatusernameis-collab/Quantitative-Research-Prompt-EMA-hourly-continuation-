# EMA Hourly Continuation — MOODENG/USDT P8_50

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.8659 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0545 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.2507 |
| sortino_ratio | -0.4692 |
| max_drawdown | 0.4695 |
| cagr | -0.1983 |
| net_avg_win | 82.1159 |
| net_avg_loss | -99.6773 |
| avg_hold_time_bars | 13.6192 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
