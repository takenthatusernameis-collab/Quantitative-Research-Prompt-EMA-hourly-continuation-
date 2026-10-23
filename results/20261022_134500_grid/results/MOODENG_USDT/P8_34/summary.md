# EMA Hourly Continuation — MOODENG/USDT P8_34

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -6.7351 |
| sortino_ratio | -3.4510 |
| max_drawdown | 0.9715 |
| cagr | -0.8138 |
| net_avg_win | 30.2733 |
| net_avg_loss | -43.1303 |
| avg_hold_time_bars | 5.8093 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
