# EMA Hourly Continuation — HBAR/USDT P8_20

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8001 |
| net_win_rate | 0.5377 |
| gross_profit_factor | 1.1513 |
| gross_win_rate | 0.5377 |
| sharpe_ratio | -1.5317 |
| sortino_ratio | -0.4839 |
| max_drawdown | 0.4463 |
| cagr | -0.1994 |
| net_avg_win | 66.6564 |
| net_avg_loss | -96.8760 |
| avg_hold_time_bars | 5.1611 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
