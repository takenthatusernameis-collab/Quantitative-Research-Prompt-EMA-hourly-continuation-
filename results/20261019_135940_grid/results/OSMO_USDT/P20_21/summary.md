# EMA Hourly Continuation — OSMO/USDT P20_21

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.1424 |
| net_win_rate | 0.2678 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.3693 |
| sharpe_ratio | -18.8526 |
| sortino_ratio | -10.2319 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 4.9141 |
| net_avg_loss | -12.6201 |
| avg_hold_time_bars | 2.0650 |
| exposure | 0.1185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
