# EMA Hourly Continuation — MOODENG/USDT P89_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.8197 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.0197 |
| sortino_ratio | -0.2414 |
| max_drawdown | 0.2460 |
| cagr | -0.1059 |
| net_avg_win | 83.7166 |
| net_avg_loss | -101.2318 |
| avg_hold_time_bars | 18.2489 |
| exposure | 0.2272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
