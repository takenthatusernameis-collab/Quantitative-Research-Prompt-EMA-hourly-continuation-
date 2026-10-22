# EMA Hourly Continuation — OSMO/USDT P26_100

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7546 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.0958 |
| sortino_ratio | -0.6521 |
| max_drawdown | 0.5590 |
| cagr | -0.2594 |
| net_avg_win | 70.4950 |
| net_avg_loss | -88.8062 |
| avg_hold_time_bars | 16.2278 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
