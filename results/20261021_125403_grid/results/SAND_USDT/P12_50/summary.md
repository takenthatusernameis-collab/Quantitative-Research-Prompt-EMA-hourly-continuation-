# EMA Hourly Continuation — SAND/USDT P12_50

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -2.5865 |
| sortino_ratio | -0.9122 |
| max_drawdown | 0.6813 |
| cagr | -0.3424 |
| net_avg_win | 54.5696 |
| net_avg_loss | -72.6365 |
| avg_hold_time_bars | 12.5115 |
| exposure | 0.3458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
