# EMA Hourly Continuation — CELR/USDT P144_200

**Symbol:** CELR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -4.9414 |
| sortino_ratio | -1.4390 |
| max_drawdown | 0.8255 |
| cagr | -0.4977 |
| net_avg_win | 36.3702 |
| net_avg_loss | -62.3231 |
| avg_hold_time_bars | 4.8839 |
| exposure | 0.0933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
