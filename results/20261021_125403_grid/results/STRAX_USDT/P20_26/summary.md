# EMA Hourly Continuation — STRAX/USDT P20_26

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.7144 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -5.2426 |
| sortino_ratio | -1.5792 |
| max_drawdown | 0.8388 |
| cagr | -0.5186 |
| net_avg_win | 36.7824 |
| net_avg_loss | -58.9728 |
| avg_hold_time_bars | 6.0113 |
| exposure | 0.1212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
