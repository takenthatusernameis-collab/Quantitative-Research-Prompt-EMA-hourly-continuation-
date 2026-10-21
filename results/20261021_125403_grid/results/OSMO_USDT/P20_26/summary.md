# EMA Hourly Continuation — OSMO/USDT P20_26

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4146 |
| gross_profit_factor | 0.8126 |
| gross_win_rate | 0.4146 |
| sharpe_ratio | -4.3660 |
| sortino_ratio | -1.1130 |
| max_drawdown | 0.7330 |
| cagr | -0.4033 |
| net_avg_win | 58.2020 |
| net_avg_loss | -80.4869 |
| avg_hold_time_bars | 4.9937 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
