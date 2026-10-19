# EMA Hourly Continuation — PENDLE/USDT P20_21

**Symbol:** PENDLE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.2106 |
| net_win_rate | 0.3246 |
| gross_profit_factor | 0.6807 |
| gross_win_rate | 0.3816 |
| sharpe_ratio | -16.6102 |
| sortino_ratio | -8.7052 |
| max_drawdown | 1.0000 |
| cagr | -0.9924 |
| net_avg_win | 6.5065 |
| net_avg_loss | -14.8507 |
| avg_hold_time_bars | 1.7023 |
| exposure | 0.0977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
