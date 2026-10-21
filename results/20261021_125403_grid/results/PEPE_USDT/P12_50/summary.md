# EMA Hourly Continuation — PEPE/USDT P12_50

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.8071 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.7316 |
| sortino_ratio | -0.5975 |
| max_drawdown | 0.5385 |
| cagr | -0.2412 |
| net_avg_win | 72.4026 |
| net_avg_loss | -88.7804 |
| avg_hold_time_bars | 10.7642 |
| exposure | 0.2843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
