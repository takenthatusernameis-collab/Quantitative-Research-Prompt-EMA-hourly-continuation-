# EMA Hourly Continuation — LINK/USDT P50_200

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.8296 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0468 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -0.9403 |
| sortino_ratio | -0.2308 |
| max_drawdown | 0.3168 |
| cagr | -0.1014 |
| net_avg_win | 76.4801 |
| net_avg_loss | -97.3790 |
| avg_hold_time_bars | 25.6404 |
| exposure | 0.3403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
