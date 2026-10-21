# EMA Hourly Continuation — GALA/USDT P26_100

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -1.9512 |
| sortino_ratio | -0.5785 |
| max_drawdown | 0.5064 |
| cagr | -0.2337 |
| net_avg_win | 64.0518 |
| net_avg_loss | -79.6014 |
| avg_hold_time_bars | 17.8268 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
