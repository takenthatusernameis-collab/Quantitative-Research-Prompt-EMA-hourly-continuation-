# EMA Hourly Continuation — MOODENG/USDT P20_21

**Symbol:** MOODENG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.2636 |
| net_win_rate | 0.3041 |
| gross_profit_factor | 0.5837 |
| gross_win_rate | 0.3736 |
| sharpe_ratio | -17.0318 |
| sortino_ratio | -8.9418 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 11.3633 |
| net_avg_loss | -18.8337 |
| avg_hold_time_bars | 2.0212 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
