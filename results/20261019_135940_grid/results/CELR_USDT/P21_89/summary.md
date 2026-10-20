# EMA Hourly Continuation — CELR/USDT P21_89

**Symbol:** CELR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.0618 |
| sortino_ratio | -1.5318 |
| max_drawdown | 0.8480 |
| cagr | -0.5151 |
| net_avg_win | 42.1471 |
| net_avg_loss | -59.6109 |
| avg_hold_time_bars | 12.2668 |
| exposure | 0.3974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
