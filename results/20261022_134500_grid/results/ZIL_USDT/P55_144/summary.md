# EMA Hourly Continuation — ZIL/USDT P55_144

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -3.6654 |
| sortino_ratio | -1.1469 |
| max_drawdown | 0.7488 |
| cagr | -0.4213 |
| net_avg_win | 42.2286 |
| net_avg_loss | -67.0812 |
| avg_hold_time_bars | 12.3625 |
| exposure | 0.2759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
