# EMA Hourly Continuation — MOODENG/USDT P50_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.2910 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.5735 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -10.6104 |
| sortino_ratio | -4.3979 |
| max_drawdown | 0.9920 |
| cagr | -0.9035 |
| net_avg_win | 15.0799 |
| net_avg_loss | -32.9206 |
| avg_hold_time_bars | 2.1770 |
| exposure | 0.0837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
