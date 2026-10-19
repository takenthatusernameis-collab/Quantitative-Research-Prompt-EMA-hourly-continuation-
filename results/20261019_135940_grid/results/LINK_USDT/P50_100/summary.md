# EMA Hourly Continuation — LINK/USDT P50_100

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -5.5275 |
| sortino_ratio | -1.9013 |
| max_drawdown | 0.9083 |
| cagr | -0.6097 |
| net_avg_win | 33.8826 |
| net_avg_loss | -57.7438 |
| avg_hold_time_bars | 5.8946 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
