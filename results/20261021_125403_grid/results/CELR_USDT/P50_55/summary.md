# EMA Hourly Continuation — CELR/USDT P50_55

**Symbol:** CELR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9250 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.3130 |
| sortino_ratio | -0.4939 |
| max_drawdown | 0.4567 |
| cagr | -0.2023 |
| net_avg_win | 65.1039 |
| net_avg_loss | -96.9587 |
| avg_hold_time_bars | 4.8559 |
| exposure | 0.0488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
