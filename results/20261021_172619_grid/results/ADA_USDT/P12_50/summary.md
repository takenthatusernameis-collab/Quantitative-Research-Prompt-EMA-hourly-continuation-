# EMA Hourly Continuation — ADA/USDT P12_50

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7634 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.0352 |
| sortino_ratio | -0.7157 |
| max_drawdown | 0.5986 |
| cagr | -0.2806 |
| net_avg_win | 60.1387 |
| net_avg_loss | -79.5626 |
| avg_hold_time_bars | 10.9168 |
| exposure | 0.2982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
