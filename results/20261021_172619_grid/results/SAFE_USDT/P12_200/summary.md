# EMA Hourly Continuation — SAFE/USDT P12_200

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.9002 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.5546 |
| sortino_ratio | -0.1406 |
| max_drawdown | 0.1973 |
| cagr | -0.0660 |
| net_avg_win | 88.2305 |
| net_avg_loss | -104.5471 |
| avg_hold_time_bars | 51.5387 |
| exposure | 0.7317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
