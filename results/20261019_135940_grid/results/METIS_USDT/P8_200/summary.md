# EMA Hourly Continuation — METIS/USDT P8_200

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9051 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -2.4602 |
| sortino_ratio | -0.6151 |
| max_drawdown | 0.5329 |
| cagr | -0.2580 |
| net_avg_win | 69.1668 |
| net_avg_loss | -90.0549 |
| avg_hold_time_bars | 55.6087 |
| exposure | 0.8139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
