# EMA Hourly Continuation — CATI/USDT P8_200

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -4.2395 |
| sortino_ratio | -1.2130 |
| max_drawdown | 0.7373 |
| cagr | -0.4472 |
| net_avg_win | 55.3687 |
| net_avg_loss | -79.3926 |
| avg_hold_time_bars | 41.3496 |
| exposure | 0.7910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
