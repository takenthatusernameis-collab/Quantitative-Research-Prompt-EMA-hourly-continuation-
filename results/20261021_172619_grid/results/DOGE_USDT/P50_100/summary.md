# EMA Hourly Continuation — DOGE/USDT P50_100

**Symbol:** DOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6413 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -2.3469 |
| sortino_ratio | -0.6058 |
| max_drawdown | 0.5057 |
| cagr | -0.2418 |
| net_avg_win | 57.7902 |
| net_avg_loss | -81.6801 |
| avg_hold_time_bars | 10.3313 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
