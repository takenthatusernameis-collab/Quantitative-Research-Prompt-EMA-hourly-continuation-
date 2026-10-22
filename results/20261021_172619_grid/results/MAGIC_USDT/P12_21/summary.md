# EMA Hourly Continuation — MAGIC/USDT P12_21

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6546 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9547 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.8019 |
| sortino_ratio | -1.2756 |
| max_drawdown | 0.7855 |
| cagr | -0.4437 |
| net_avg_win | 56.6108 |
| net_avg_loss | -76.6743 |
| avg_hold_time_bars | 5.3443 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
