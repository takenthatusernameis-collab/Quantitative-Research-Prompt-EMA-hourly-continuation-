# EMA Hourly Continuation — JASMY/USDT P50_144

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7768 |
| net_win_rate | 0.5413 |
| gross_profit_factor | 1.1546 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -1.5525 |
| sortino_ratio | -0.4829 |
| max_drawdown | 0.4668 |
| cagr | -0.2079 |
| net_avg_win | 58.8536 |
| net_avg_loss | -89.4134 |
| avg_hold_time_bars | 12.0393 |
| exposure | 0.2649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
