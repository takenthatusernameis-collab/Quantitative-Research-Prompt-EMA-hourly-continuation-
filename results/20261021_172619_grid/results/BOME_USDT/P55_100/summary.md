# EMA Hourly Continuation — BOME/USDT P55_100

**Symbol:** BOME/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8068 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0047 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.1280 |
| sortino_ratio | -0.3081 |
| max_drawdown | 0.3623 |
| cagr | -0.1334 |
| net_avg_win | 68.5470 |
| net_avg_loss | -87.8286 |
| avg_hold_time_bars | 8.2044 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
