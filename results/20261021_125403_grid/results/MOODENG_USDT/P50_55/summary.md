# EMA Hourly Continuation — MOODENG/USDT P50_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 106 |
| net_profit_factor | 0.5798 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.7926 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -1.9191 |
| sortino_ratio | -0.3098 |
| max_drawdown | 0.2757 |
| cagr | -0.1326 |
| net_avg_win | 74.6393 |
| net_avg_loss | -102.5558 |
| avg_hold_time_bars | 6.2547 |
| exposure | 0.0367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
