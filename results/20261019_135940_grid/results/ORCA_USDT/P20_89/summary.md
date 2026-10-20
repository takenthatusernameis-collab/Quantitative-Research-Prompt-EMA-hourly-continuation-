# EMA Hourly Continuation — ORCA/USDT P20_89

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5689 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8538 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -4.1184 |
| sortino_ratio | -1.4575 |
| max_drawdown | 0.8480 |
| cagr | -0.5056 |
| net_avg_win | 36.7367 |
| net_avg_loss | -56.7614 |
| avg_hold_time_bars | 14.3579 |
| exposure | 0.4157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
