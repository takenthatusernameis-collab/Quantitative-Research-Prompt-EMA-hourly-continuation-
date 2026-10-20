# EMA Hourly Continuation — BOME/USDT P100_200

**Symbol:** BOME/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.6394 |
| sortino_ratio | -0.7214 |
| max_drawdown | 0.5968 |
| cagr | -0.2888 |
| net_avg_win | 47.5381 |
| net_avg_loss | -74.8731 |
| avg_hold_time_bars | 10.1755 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
