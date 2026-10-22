# EMA Hourly Continuation — TRAC/USDT P12_200

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5983 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -3.5718 |
| sortino_ratio | -1.0225 |
| max_drawdown | 0.7187 |
| cagr | -0.3866 |
| net_avg_win | 57.8412 |
| net_avg_loss | -73.6243 |
| avg_hold_time_bars | 35.8599 |
| exposure | 0.6862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
