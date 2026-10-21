# EMA Hourly Continuation — VELO/USDT P50_100

**Symbol:** VELO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7958 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.3044 |
| sortino_ratio | -0.3607 |
| max_drawdown | 0.3932 |
| cagr | -0.1535 |
| net_avg_win | 71.2442 |
| net_avg_loss | -90.0078 |
| avg_hold_time_bars | 8.9169 |
| exposure | 0.1512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
