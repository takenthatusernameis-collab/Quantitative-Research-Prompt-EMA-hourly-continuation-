# EMA Hourly Continuation — SAFE/USDT P8_200

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.9356 |
| sortino_ratio | -0.5494 |
| max_drawdown | 0.5035 |
| cagr | -0.2320 |
| net_avg_win | 69.8930 |
| net_avg_loss | -91.8138 |
| avg_hold_time_bars | 42.0025 |
| exposure | 0.7752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
