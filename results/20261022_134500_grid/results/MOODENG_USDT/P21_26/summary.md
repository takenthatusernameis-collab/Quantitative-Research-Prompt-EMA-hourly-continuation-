# EMA Hourly Continuation — MOODENG/USDT P21_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1025 |
| net_profit_factor | 0.3654 |
| net_win_rate | 0.3580 |
| gross_profit_factor | 0.6916 |
| gross_win_rate | 0.4010 |
| sharpe_ratio | -13.6649 |
| sortino_ratio | -6.9020 |
| max_drawdown | 0.9994 |
| cagr | -0.9733 |
| net_avg_win | 15.6819 |
| net_avg_loss | -23.9356 |
| avg_hold_time_bars | 2.1278 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
