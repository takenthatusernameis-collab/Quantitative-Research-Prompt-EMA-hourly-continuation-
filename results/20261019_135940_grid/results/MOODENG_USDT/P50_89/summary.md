# EMA Hourly Continuation — MOODENG/USDT P50_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5364 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8044 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -5.0033 |
| sortino_ratio | -1.8287 |
| max_drawdown | 0.8350 |
| cagr | -0.5825 |
| net_avg_win | 38.8043 |
| net_avg_loss | -59.4466 |
| avg_hold_time_bars | 5.4982 |
| exposure | 0.1679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
