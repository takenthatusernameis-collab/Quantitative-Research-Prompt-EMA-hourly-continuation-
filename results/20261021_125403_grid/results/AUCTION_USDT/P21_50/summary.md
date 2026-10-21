# EMA Hourly Continuation — AUCTION/USDT P21_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -4.9000 |
| sortino_ratio | -1.7089 |
| max_drawdown | 0.8715 |
| cagr | -0.5509 |
| net_avg_win | 42.6002 |
| net_avg_loss | -59.9143 |
| avg_hold_time_bars | 7.6545 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
