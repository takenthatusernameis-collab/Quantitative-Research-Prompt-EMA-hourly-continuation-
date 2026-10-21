# EMA Hourly Continuation — CGPT/USDT P8_200

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.8902 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0262 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -0.6084 |
| sortino_ratio | -0.1510 |
| max_drawdown | 0.2277 |
| cagr | -0.0702 |
| net_avg_win | 89.1334 |
| net_avg_loss | -102.8290 |
| avg_hold_time_bars | 57.9833 |
| exposure | 0.7907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
