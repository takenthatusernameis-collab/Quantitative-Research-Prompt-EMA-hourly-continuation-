# EMA Hourly Continuation — NEAR/USDT P21_100

**Symbol:** NEAR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7831 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.5437 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4639 |
| cagr | -0.1891 |
| net_avg_win | 72.1074 |
| net_avg_loss | -87.3860 |
| avg_hold_time_bars | 20.1663 |
| exposure | 0.3859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
