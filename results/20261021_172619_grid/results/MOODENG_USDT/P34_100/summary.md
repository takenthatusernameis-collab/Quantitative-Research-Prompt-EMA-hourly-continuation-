# EMA Hourly Continuation — MOODENG/USDT P34_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7501 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -1.9137 |
| sortino_ratio | -0.5492 |
| max_drawdown | 0.4204 |
| cagr | -0.2239 |
| net_avg_win | 77.3813 |
| net_avg_loss | -92.6072 |
| avg_hold_time_bars | 14.4940 |
| exposure | 0.2679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
