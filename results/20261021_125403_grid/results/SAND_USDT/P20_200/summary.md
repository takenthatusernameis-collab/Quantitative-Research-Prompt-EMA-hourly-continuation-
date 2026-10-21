# EMA Hourly Continuation — SAND/USDT P20_200

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6882 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8385 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -1.9055 |
| sortino_ratio | -0.4315 |
| max_drawdown | 0.4054 |
| cagr | -0.1806 |
| net_avg_win | 74.8812 |
| net_avg_loss | -90.8025 |
| avg_hold_time_bars | 57.5020 |
| exposure | 0.6665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
