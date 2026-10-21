# EMA Hourly Continuation — DUSK/USDT P50_100

**Symbol:** DUSK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7487 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.8010 |
| sortino_ratio | -0.5321 |
| max_drawdown | 0.4755 |
| cagr | -0.2174 |
| net_avg_win | 65.5369 |
| net_avg_loss | -83.9214 |
| avg_hold_time_bars | 7.9906 |
| exposure | 0.1551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
