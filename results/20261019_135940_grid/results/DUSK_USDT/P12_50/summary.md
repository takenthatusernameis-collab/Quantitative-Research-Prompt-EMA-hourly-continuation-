# EMA Hourly Continuation — DUSK/USDT P12_50

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.6661 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 1.0283 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -5.5977 |
| sortino_ratio | -2.5383 |
| max_drawdown | 0.9567 |
| cagr | -0.7046 |
| net_avg_win | 39.5301 |
| net_avg_loss | -50.7035 |
| avg_hold_time_bars | 7.5967 |
| exposure | 0.3605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
