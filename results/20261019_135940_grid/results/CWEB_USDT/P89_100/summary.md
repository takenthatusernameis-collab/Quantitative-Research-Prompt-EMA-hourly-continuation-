# EMA Hourly Continuation — CWEB/USDT P89_100

**Symbol:** CWEB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.2218 |
| net_win_rate | 0.2549 |
| gross_profit_factor | 0.6311 |
| gross_win_rate | 0.2941 |
| sharpe_ratio | -11.8789 |
| sortino_ratio | -4.1076 |
| max_drawdown | 0.9967 |
| cagr | -0.8969 |
| net_avg_win | 21.8481 |
| net_avg_loss | -33.7027 |
| avg_hold_time_bars | 3.4412 |
| exposure | 0.0798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
