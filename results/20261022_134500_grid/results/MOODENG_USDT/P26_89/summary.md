# EMA Hourly Continuation — MOODENG/USDT P26_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6168 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8701 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.2276 |
| sortino_ratio | -1.6006 |
| max_drawdown | 0.7983 |
| cagr | -0.5329 |
| net_avg_win | 47.0353 |
| net_avg_loss | -64.1831 |
| avg_hold_time_bars | 10.0118 |
| exposure | 0.3285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
