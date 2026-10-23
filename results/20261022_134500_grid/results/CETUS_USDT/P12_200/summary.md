# EMA Hourly Continuation — CETUS/USDT P12_200

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9316 |
| net_win_rate | 0.5478 |
| gross_profit_factor | 1.2506 |
| gross_win_rate | 0.5551 |
| sharpe_ratio | -0.3255 |
| sortino_ratio | -0.0755 |
| max_drawdown | 0.2188 |
| cagr | -0.0398 |
| net_avg_win | 89.0991 |
| net_avg_loss | -115.8526 |
| avg_hold_time_bars | 66.7757 |
| exposure | 0.8219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
