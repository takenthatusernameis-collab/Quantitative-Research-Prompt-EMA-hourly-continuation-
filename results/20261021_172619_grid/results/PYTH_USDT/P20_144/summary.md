# EMA Hourly Continuation — PYTH/USDT P20_144

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8370 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.1126 |
| sortino_ratio | -0.3108 |
| max_drawdown | 0.3712 |
| cagr | -0.1354 |
| net_avg_win | 83.1513 |
| net_avg_loss | -97.2809 |
| avg_hold_time_bars | 31.2382 |
| exposure | 0.5424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
