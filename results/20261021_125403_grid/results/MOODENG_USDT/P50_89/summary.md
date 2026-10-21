# EMA Hourly Continuation — MOODENG/USDT P50_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.0106 |
| sortino_ratio | -0.5309 |
| max_drawdown | 0.4302 |
| cagr | -0.2170 |
| net_avg_win | 77.3280 |
| net_avg_loss | -96.7900 |
| avg_hold_time_bars | 8.9397 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
