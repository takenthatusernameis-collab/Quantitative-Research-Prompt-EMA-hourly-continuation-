# EMA Hourly Continuation — EGLD/USDT P21_55

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -7.1928 |
| sortino_ratio | -3.1425 |
| max_drawdown | 0.9799 |
| cagr | -0.7870 |
| net_avg_win | 20.3295 |
| net_avg_loss | -35.3756 |
| avg_hold_time_bars | 5.5109 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
