# EMA Hourly Continuation — SAND/USDT P34_100

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.8017 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.4323 |
| sortino_ratio | -0.4145 |
| max_drawdown | 0.4326 |
| cagr | -0.1738 |
| net_avg_win | 74.4058 |
| net_avg_loss | -96.5412 |
| avg_hold_time_bars | 12.9581 |
| exposure | 0.2391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
