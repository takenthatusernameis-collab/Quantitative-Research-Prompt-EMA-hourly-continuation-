# EMA Hourly Continuation — POPCAT/USDT P50_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -3.1543 |
| sortino_ratio | -0.9954 |
| max_drawdown | 0.6446 |
| cagr | -0.3753 |
| net_avg_win | 57.4540 |
| net_avg_loss | -76.4599 |
| avg_hold_time_bars | 14.5486 |
| exposure | 0.3320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
