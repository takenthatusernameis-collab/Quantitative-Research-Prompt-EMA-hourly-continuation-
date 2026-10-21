# EMA Hourly Continuation — DEXE/USDT P8_21

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7094 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -2.0987 |
| sortino_ratio | -0.6962 |
| max_drawdown | 0.5685 |
| cagr | -0.2743 |
| net_avg_win | 49.4353 |
| net_avg_loss | -73.1750 |
| avg_hold_time_bars | 9.9118 |
| exposure | 0.2401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
