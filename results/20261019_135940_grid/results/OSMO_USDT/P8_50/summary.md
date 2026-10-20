# EMA Hourly Continuation — OSMO/USDT P8_50

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -7.0484 |
| sortino_ratio | -3.2908 |
| max_drawdown | 0.9817 |
| cagr | -0.7962 |
| net_avg_win | 31.2942 |
| net_avg_loss | -41.0947 |
| avg_hold_time_bars | 9.5209 |
| exposure | 0.4769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
