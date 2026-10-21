# EMA Hourly Continuation — MEME/USDT P20_21

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.6204 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.1250 |
| sortino_ratio | -0.4016 |
| max_drawdown | 0.4308 |
| cagr | -0.1689 |
| net_avg_win | 75.9131 |
| net_avg_loss | -103.0465 |
| avg_hold_time_bars | 4.9600 |
| exposure | 0.0395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
