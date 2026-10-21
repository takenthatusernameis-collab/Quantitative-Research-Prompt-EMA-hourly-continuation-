# EMA Hourly Continuation — BRETT/USDT P12_200

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.9564 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -0.1772 |
| sortino_ratio | -0.0405 |
| max_drawdown | 0.1536 |
| cagr | -0.0225 |
| net_avg_win | 93.6579 |
| net_avg_loss | -104.7424 |
| avg_hold_time_bars | 68.4958 |
| exposure | 0.7844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
