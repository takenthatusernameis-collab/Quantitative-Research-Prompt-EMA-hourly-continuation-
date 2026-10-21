# EMA Hourly Continuation — ASTR/USDT P12_144

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7948 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.4205 |
| sortino_ratio | -0.3877 |
| max_drawdown | 0.4436 |
| cagr | -0.1651 |
| net_avg_win | 78.2434 |
| net_avg_loss | -95.7996 |
| avg_hold_time_bars | 41.9346 |
| exposure | 0.6964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
