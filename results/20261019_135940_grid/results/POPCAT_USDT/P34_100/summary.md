# EMA Hourly Continuation — POPCAT/USDT P34_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.5809 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -4.8074 |
| sortino_ratio | -1.7670 |
| max_drawdown | 0.8403 |
| cagr | -0.5719 |
| net_avg_win | 45.1251 |
| net_avg_loss | -60.1905 |
| avg_hold_time_bars | 9.6954 |
| exposure | 0.3027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
