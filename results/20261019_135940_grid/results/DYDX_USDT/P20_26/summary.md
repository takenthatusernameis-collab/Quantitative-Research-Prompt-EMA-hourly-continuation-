# EMA Hourly Continuation — DYDX/USDT P20_26

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.3252 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -12.7839 |
| sortino_ratio | -6.4285 |
| max_drawdown | 0.9998 |
| cagr | -0.9653 |
| net_avg_win | 9.7355 |
| net_avg_loss | -20.0771 |
| avg_hold_time_bars | 1.9440 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
