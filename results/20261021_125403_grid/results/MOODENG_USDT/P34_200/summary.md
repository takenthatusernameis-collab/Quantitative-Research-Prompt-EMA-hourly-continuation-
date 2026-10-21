# EMA Hourly Continuation — MOODENG/USDT P34_200

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.8916 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -0.5932 |
| sortino_ratio | -0.1449 |
| max_drawdown | 0.2118 |
| cagr | -0.0676 |
| net_avg_win | 91.3498 |
| net_avg_loss | -105.0622 |
| avg_hold_time_bars | 39.7573 |
| exposure | 0.5258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
