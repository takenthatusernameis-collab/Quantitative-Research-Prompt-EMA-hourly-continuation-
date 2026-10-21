# EMA Hourly Continuation — STRAX/USDT P34_200

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.5428 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.7108 |
| gross_win_rate | 0.4177 |
| sharpe_ratio | -3.9168 |
| sortino_ratio | -1.1358 |
| max_drawdown | 0.7303 |
| cagr | -0.4084 |
| net_avg_win | 49.5460 |
| net_avg_loss | -65.4670 |
| avg_hold_time_bars | 22.6062 |
| exposure | 0.4331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
