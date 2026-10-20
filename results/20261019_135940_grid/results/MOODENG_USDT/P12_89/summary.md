# EMA Hourly Continuation — MOODENG/USDT P12_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.6461 |
| sortino_ratio | -1.3536 |
| max_drawdown | 0.7504 |
| cagr | -0.4743 |
| net_avg_win | 57.8481 |
| net_avg_loss | -73.8112 |
| avg_hold_time_bars | 17.1167 |
| exposure | 0.5436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
