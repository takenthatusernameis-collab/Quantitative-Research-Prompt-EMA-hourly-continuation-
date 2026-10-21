# EMA Hourly Continuation — POLYX/USDT P21_34

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6411 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -3.3351 |
| sortino_ratio | -1.0147 |
| max_drawdown | 0.7049 |
| cagr | -0.3715 |
| net_avg_win | 56.6716 |
| net_avg_loss | -82.6839 |
| avg_hold_time_bars | 4.9822 |
| exposure | 0.1017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
