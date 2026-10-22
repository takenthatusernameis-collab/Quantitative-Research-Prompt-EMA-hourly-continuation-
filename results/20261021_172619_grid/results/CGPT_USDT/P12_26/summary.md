# EMA Hourly Continuation — CGPT/USDT P12_26

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7540 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0135 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.9356 |
| sortino_ratio | -0.5812 |
| max_drawdown | 0.5295 |
| cagr | -0.2334 |
| net_avg_win | 67.8776 |
| net_avg_loss | -91.2620 |
| avg_hold_time_bars | 5.4668 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
