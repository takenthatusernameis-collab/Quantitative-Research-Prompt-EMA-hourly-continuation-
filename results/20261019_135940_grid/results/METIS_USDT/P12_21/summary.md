# EMA Hourly Continuation — METIS/USDT P12_21

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1499 |
| net_profit_factor | 0.3090 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -12.9544 |
| sortino_ratio | -7.1356 |
| max_drawdown | 0.9999 |
| cagr | -0.9739 |
| net_avg_win | 7.3768 |
| net_avg_loss | -16.2030 |
| avg_hold_time_bars | 2.4850 |
| exposure | 0.1693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
