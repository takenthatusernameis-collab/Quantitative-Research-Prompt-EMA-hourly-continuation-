# EMA Hourly Continuation — STRK/USDT P20_26

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 172 |
| net_profit_factor | 0.5878 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -2.1343 |
| sortino_ratio | -0.3981 |
| max_drawdown | 0.3790 |
| cagr | -0.1670 |
| net_avg_win | 69.0407 |
| net_avg_loss | -92.9877 |
| avg_hold_time_bars | 5.0465 |
| exposure | 0.0395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
