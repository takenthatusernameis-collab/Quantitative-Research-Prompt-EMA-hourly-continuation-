# EMA Hourly Continuation — BAND/USDT P12_50

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0599 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -2.3123 |
| sortino_ratio | -0.8704 |
| max_drawdown | 0.6873 |
| cagr | -0.3305 |
| net_avg_win | 69.8488 |
| net_avg_loss | -90.0363 |
| avg_hold_time_bars | 11.2752 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
