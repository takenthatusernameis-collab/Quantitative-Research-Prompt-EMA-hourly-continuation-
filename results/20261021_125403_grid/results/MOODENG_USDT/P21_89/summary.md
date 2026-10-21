# EMA Hourly Continuation — MOODENG/USDT P21_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7958 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.7476 |
| sortino_ratio | -0.5644 |
| max_drawdown | 0.4811 |
| cagr | -0.2303 |
| net_avg_win | 79.3063 |
| net_avg_loss | -94.5822 |
| avg_hold_time_bars | 15.3088 |
| exposure | 0.3566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
