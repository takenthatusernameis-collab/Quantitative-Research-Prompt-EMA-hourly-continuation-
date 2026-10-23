# EMA Hourly Continuation — MOVR/USDT P20_144

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5341 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.7871 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -4.2624 |
| sortino_ratio | -1.4485 |
| max_drawdown | 0.8288 |
| cagr | -0.5005 |
| net_avg_win | 36.6560 |
| net_avg_loss | -53.3356 |
| avg_hold_time_bars | 20.1441 |
| exposure | 0.5402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
