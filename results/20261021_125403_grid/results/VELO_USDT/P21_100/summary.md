# EMA Hourly Continuation — VELO/USDT P21_100

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.8959 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0572 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -0.6863 |
| sortino_ratio | -0.2188 |
| max_drawdown | 0.3821 |
| cagr | -0.1005 |
| net_avg_win | 78.8327 |
| net_avg_loss | -94.6773 |
| avg_hold_time_bars | 16.9289 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
