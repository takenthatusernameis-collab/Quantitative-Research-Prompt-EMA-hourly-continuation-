# EMA Hourly Continuation — PEPE/USDT P100_200

**Symbol:** PEPE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5793 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -3.6940 |
| sortino_ratio | -1.0381 |
| max_drawdown | 0.7169 |
| cagr | -0.3915 |
| net_avg_win | 54.8403 |
| net_avg_loss | -76.6715 |
| avg_hold_time_bars | 9.1475 |
| exposure | 0.1663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
