# EMA Hourly Continuation — VELO/USDT P50_200

**Symbol:** VELO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8980 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0424 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.5415 |
| sortino_ratio | -0.1411 |
| max_drawdown | 0.2442 |
| cagr | -0.0664 |
| net_avg_win | 82.1139 |
| net_avg_loss | -97.1529 |
| avg_hold_time_bars | 24.0303 |
| exposure | 0.3605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
