# EMA Hourly Continuation — MOODENG/USDT P26_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.6205 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.0739 |
| sortino_ratio | -1.4887 |
| max_drawdown | 0.7718 |
| cagr | -0.5073 |
| net_avg_win | 50.0125 |
| net_avg_loss | -66.7706 |
| avg_hold_time_bars | 11.9747 |
| exposure | 0.3671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
