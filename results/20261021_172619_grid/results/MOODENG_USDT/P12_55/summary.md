# EMA Hourly Continuation — MOODENG/USDT P12_55

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -1.8873 |
| sortino_ratio | -0.6785 |
| max_drawdown | 0.5337 |
| cagr | -0.2700 |
| net_avg_win | 74.5220 |
| net_avg_loss | -90.0128 |
| avg_hold_time_bars | 12.3724 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
