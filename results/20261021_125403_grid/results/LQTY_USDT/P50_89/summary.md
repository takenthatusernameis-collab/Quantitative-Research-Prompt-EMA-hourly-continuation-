# EMA Hourly Continuation — LQTY/USDT P50_89

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5964 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -3.2004 |
| sortino_ratio | -0.9112 |
| max_drawdown | 0.6538 |
| cagr | -0.3415 |
| net_avg_win | 53.1897 |
| net_avg_loss | -73.0391 |
| avg_hold_time_bars | 7.3358 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
