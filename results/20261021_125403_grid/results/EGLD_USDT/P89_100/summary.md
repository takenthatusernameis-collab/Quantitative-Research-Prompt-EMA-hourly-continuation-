# EMA Hourly Continuation — EGLD/USDT P89_100

**Symbol:** EGLD/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 121 |
| net_profit_factor | 0.8018 |
| net_win_rate | 0.5537 |
| gross_profit_factor | 1.2173 |
| gross_win_rate | 0.5537 |
| sharpe_ratio | -0.6817 |
| sortino_ratio | -0.1090 |
| max_drawdown | 0.1471 |
| cagr | -0.0485 |
| net_avg_win | 70.8800 |
| net_avg_loss | -109.6869 |
| avg_hold_time_bars | 4.4050 |
| exposure | 0.0242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
