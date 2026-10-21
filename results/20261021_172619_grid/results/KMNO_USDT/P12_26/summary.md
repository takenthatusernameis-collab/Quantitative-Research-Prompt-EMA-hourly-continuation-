# EMA Hourly Continuation — KMNO/USDT P12_26

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1140 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -1.4960 |
| sortino_ratio | -0.4874 |
| max_drawdown | 0.4560 |
| cagr | -0.2024 |
| net_avg_win | 63.0706 |
| net_avg_loss | -89.7735 |
| avg_hold_time_bars | 5.8294 |
| exposure | 0.1356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
