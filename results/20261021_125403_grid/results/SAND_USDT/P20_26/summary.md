# EMA Hourly Continuation — SAND/USDT P20_26

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 159 |
| net_profit_factor | 0.5522 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8061 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -2.3157 |
| sortino_ratio | -0.4176 |
| max_drawdown | 0.4294 |
| cagr | -0.1752 |
| net_avg_win | 66.6210 |
| net_avg_loss | -97.3382 |
| avg_hold_time_bars | 4.2201 |
| exposure | 0.0305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
