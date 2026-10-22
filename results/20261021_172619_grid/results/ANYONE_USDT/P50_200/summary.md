# EMA Hourly Continuation — ANYONE/USDT P50_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.8095 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.0499 |
| sortino_ratio | -0.2519 |
| max_drawdown | 0.3194 |
| cagr | -0.1110 |
| net_avg_win | 80.6110 |
| net_avg_loss | -92.7950 |
| avg_hold_time_bars | 31.1961 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
