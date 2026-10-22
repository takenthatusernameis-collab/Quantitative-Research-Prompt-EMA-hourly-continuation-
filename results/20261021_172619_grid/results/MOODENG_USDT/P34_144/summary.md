# EMA Hourly Continuation — MOODENG/USDT P34_144

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8172 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.2037 |
| sortino_ratio | -0.3251 |
| max_drawdown | 0.2907 |
| cagr | -0.1407 |
| net_avg_win | 83.3911 |
| net_avg_loss | -97.9629 |
| avg_hold_time_bars | 24.9014 |
| exposure | 0.4051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
