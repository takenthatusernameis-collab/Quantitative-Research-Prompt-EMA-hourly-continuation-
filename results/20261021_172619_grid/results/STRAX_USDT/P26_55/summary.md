# EMA Hourly Continuation — STRAX/USDT P26_55

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6095 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8873 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.8490 |
| sortino_ratio | -1.2478 |
| max_drawdown | 0.7695 |
| cagr | -0.4389 |
| net_avg_win | 49.8791 |
| net_avg_loss | -70.8647 |
| avg_hold_time_bars | 8.7417 |
| exposure | 0.2058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
