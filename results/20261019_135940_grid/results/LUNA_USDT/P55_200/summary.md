# EMA Hourly Continuation — LUNA/USDT P55_200

**Symbol:** LUNA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5462 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8721 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.9488 |
| sortino_ratio | -1.1893 |
| max_drawdown | 0.7581 |
| cagr | -0.4317 |
| net_avg_win | 43.8580 |
| net_avg_loss | -67.6242 |
| avg_hold_time_bars | 17.5187 |
| exposure | 0.3623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
