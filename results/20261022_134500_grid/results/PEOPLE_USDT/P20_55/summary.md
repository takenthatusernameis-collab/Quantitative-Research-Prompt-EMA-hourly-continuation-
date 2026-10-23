# EMA Hourly Continuation — PEOPLE/USDT P20_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.5663 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8581 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -5.8678 |
| sortino_ratio | -2.4969 |
| max_drawdown | 0.9519 |
| cagr | -0.6996 |
| net_avg_win | 29.7385 |
| net_avg_loss | -43.7235 |
| avg_hold_time_bars | 5.6870 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
