# EMA Hourly Continuation — CRV/USDT P21_50

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8534 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1139 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -1.0697 |
| sortino_ratio | -0.3334 |
| max_drawdown | 0.3642 |
| cagr | -0.1437 |
| net_avg_win | 76.3512 |
| net_avg_loss | -100.0396 |
| avg_hold_time_bars | 6.3455 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
