# EMA Hourly Continuation — MERL/USDT P8_21

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1679 |
| net_profit_factor | 0.4600 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.7299 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -9.0468 |
| sortino_ratio | -5.2409 |
| max_drawdown | 0.9982 |
| cagr | -0.9196 |
| net_avg_win | 11.3977 |
| net_avg_loss | -19.8119 |
| avg_hold_time_bars | 3.0512 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
