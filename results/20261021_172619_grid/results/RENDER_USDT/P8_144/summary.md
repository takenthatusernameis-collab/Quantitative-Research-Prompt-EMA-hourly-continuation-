# EMA Hourly Continuation — RENDER/USDT P8_144

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.9272 |
| net_win_rate | 0.5233 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5233 |
| sharpe_ratio | -0.3661 |
| sortino_ratio | -0.0982 |
| max_drawdown | 0.1964 |
| cagr | -0.0490 |
| net_avg_win | 83.5850 |
| net_avg_loss | -98.9716 |
| avg_hold_time_bars | 48.7933 |
| exposure | 0.7726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
