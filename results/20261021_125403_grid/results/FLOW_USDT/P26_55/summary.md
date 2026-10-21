# EMA Hourly Continuation — FLOW/USDT P26_55

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7095 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.5418 |
| sortino_ratio | -0.7902 |
| max_drawdown | 0.6210 |
| cagr | -0.3037 |
| net_avg_win | 63.1357 |
| net_avg_loss | -85.6481 |
| avg_hold_time_bars | 7.1847 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
