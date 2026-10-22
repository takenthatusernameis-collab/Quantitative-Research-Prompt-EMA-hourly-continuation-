# EMA Hourly Continuation — MOODENG/USDT P26_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.8816 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0398 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -0.5942 |
| sortino_ratio | -0.1310 |
| max_drawdown | 0.2018 |
| cagr | -0.0614 |
| net_avg_win | 91.2320 |
| net_avg_loss | -107.7906 |
| avg_hold_time_bars | 62.4694 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
