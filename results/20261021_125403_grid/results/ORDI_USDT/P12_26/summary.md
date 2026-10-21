# EMA Hourly Continuation — ORDI/USDT P12_26

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7295 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.0821 |
| sortino_ratio | -0.6479 |
| max_drawdown | 0.5396 |
| cagr | -0.2572 |
| net_avg_win | 61.1484 |
| net_avg_loss | -81.0324 |
| avg_hold_time_bars | 5.5360 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
