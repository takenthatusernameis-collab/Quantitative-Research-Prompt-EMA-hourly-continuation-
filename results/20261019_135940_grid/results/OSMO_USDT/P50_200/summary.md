# EMA Hourly Continuation — OSMO/USDT P50_200

**Symbol:** OSMO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.5755 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -3.2352 |
| sortino_ratio | -0.8858 |
| max_drawdown | 0.6725 |
| cagr | -0.3468 |
| net_avg_win | 51.1769 |
| net_avg_loss | -74.7514 |
| avg_hold_time_bars | 22.5643 |
| exposure | 0.3908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
