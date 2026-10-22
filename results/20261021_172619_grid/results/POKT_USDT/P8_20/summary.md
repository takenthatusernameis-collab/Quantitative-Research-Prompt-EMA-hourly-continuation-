# EMA Hourly Continuation — POKT/USDT P8_20

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6221 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4261 |
| sharpe_ratio | -4.8868 |
| sortino_ratio | -1.7469 |
| max_drawdown | 0.8731 |
| cagr | -0.5533 |
| net_avg_win | 52.7979 |
| net_avg_loss | -63.0094 |
| avg_hold_time_bars | 5.1761 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
