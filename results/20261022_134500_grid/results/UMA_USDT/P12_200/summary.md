# EMA Hourly Continuation — UMA/USDT P12_200

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.7926 |
| sortino_ratio | -0.8638 |
| max_drawdown | 0.6566 |
| cagr | -0.3395 |
| net_avg_win | 49.1334 |
| net_avg_loss | -71.8872 |
| avg_hold_time_bars | 30.1309 |
| exposure | 0.6697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
