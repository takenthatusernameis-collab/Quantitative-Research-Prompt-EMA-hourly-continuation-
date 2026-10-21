# EMA Hourly Continuation — DEEP/USDT P55_100

**Symbol:** DEEP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8980 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1257 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -0.6138 |
| sortino_ratio | -0.1618 |
| max_drawdown | 0.2672 |
| cagr | -0.0747 |
| net_avg_win | 89.7941 |
| net_avg_loss | -112.6950 |
| avg_hold_time_bars | 7.5970 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
