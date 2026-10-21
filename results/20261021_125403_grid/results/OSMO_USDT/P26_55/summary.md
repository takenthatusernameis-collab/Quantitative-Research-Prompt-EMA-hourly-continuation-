# EMA Hourly Continuation — OSMO/USDT P26_55

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -3.6662 |
| sortino_ratio | -1.1502 |
| max_drawdown | 0.7409 |
| cagr | -0.4114 |
| net_avg_win | 56.1211 |
| net_avg_loss | -74.4267 |
| avg_hold_time_bars | 7.6957 |
| exposure | 0.1690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
