# EMA Hourly Continuation — MOODENG/USDT P20_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.6086 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -5.5304 |
| sortino_ratio | -2.4448 |
| max_drawdown | 0.9157 |
| cagr | -0.6905 |
| net_avg_win | 37.7708 |
| net_avg_loss | -53.1382 |
| avg_hold_time_bars | 5.5855 |
| exposure | 0.2513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
