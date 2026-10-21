# EMA Hourly Continuation — AVAX/USDT P34_100

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8007 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0434 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.4512 |
| sortino_ratio | -0.4145 |
| max_drawdown | 0.4134 |
| cagr | -0.1739 |
| net_avg_win | 75.8293 |
| net_avg_loss | -98.6031 |
| avg_hold_time_bars | 13.8005 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
