# EMA Hourly Continuation — ENA/USDT P50_200

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8143 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -1.5343 |
| sortino_ratio | -0.3428 |
| max_drawdown | 0.3600 |
| cagr | -0.1466 |
| net_avg_win | 74.4623 |
| net_avg_loss | -86.5618 |
| avg_hold_time_bars | 30.6320 |
| exposure | 0.3481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
