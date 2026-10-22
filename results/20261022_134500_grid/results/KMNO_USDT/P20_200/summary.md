# EMA Hourly Continuation — KMNO/USDT P20_200

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6395 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -3.0660 |
| sortino_ratio | -0.8442 |
| max_drawdown | 0.6456 |
| cagr | -0.3358 |
| net_avg_win | 65.6430 |
| net_avg_loss | -83.6703 |
| avg_hold_time_bars | 33.5901 |
| exposure | 0.5940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
