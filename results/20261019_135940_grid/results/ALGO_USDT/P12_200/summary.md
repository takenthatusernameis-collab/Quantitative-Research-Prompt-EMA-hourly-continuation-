# EMA Hourly Continuation — ALGO/USDT P12_200

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.9020 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1581 |
| gross_win_rate | 0.5418 |
| sharpe_ratio | -0.4608 |
| sortino_ratio | -0.1092 |
| max_drawdown | 0.1747 |
| cagr | -0.0528 |
| net_avg_win | 79.7590 |
| net_avg_loss | -101.5504 |
| avg_hold_time_bars | 64.6436 |
| exposure | 0.8080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
