# EMA Hourly Continuation — FLOW/USDT P89_100

**Symbol:** FLOW/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.5513 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8204 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -2.0268 |
| sortino_ratio | -0.3283 |
| max_drawdown | 0.3272 |
| cagr | -0.1403 |
| net_avg_win | 66.9284 |
| net_avg_loss | -100.5921 |
| avg_hold_time_bars | 5.3594 |
| exposure | 0.0312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
