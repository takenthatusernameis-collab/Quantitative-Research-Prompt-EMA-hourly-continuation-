# EMA Hourly Continuation — BAND/USDT P8_20

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.3679 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -10.2530 |
| sortino_ratio | -5.5439 |
| max_drawdown | 0.9990 |
| cagr | -0.9348 |
| net_avg_win | 8.9741 |
| net_avg_loss | -19.2509 |
| avg_hold_time_bars | 3.6494 |
| exposure | 0.2426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
