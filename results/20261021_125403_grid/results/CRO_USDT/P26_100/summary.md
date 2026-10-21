# EMA Hourly Continuation — CRO/USDT P26_100

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.1747 |
| sortino_ratio | -0.6375 |
| max_drawdown | 0.5438 |
| cagr | -0.2528 |
| net_avg_win | 59.0172 |
| net_avg_loss | -82.1022 |
| avg_hold_time_bars | 18.2339 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
