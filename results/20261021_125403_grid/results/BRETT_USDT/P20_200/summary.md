# EMA Hourly Continuation — BRETT/USDT P20_200

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.8667 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -0.6621 |
| sortino_ratio | -0.1443 |
| max_drawdown | 0.1689 |
| cagr | -0.0663 |
| net_avg_win | 90.3582 |
| net_avg_loss | -100.5372 |
| avg_hold_time_bars | 64.4636 |
| exposure | 0.6824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
