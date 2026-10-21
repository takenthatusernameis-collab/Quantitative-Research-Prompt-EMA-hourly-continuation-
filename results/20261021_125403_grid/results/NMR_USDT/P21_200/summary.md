# EMA Hourly Continuation — NMR/USDT P21_200

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.4974 |
| sortino_ratio | -0.3947 |
| max_drawdown | 0.4239 |
| cagr | -0.1671 |
| net_avg_win | 66.2551 |
| net_avg_loss | -82.9354 |
| avg_hold_time_bars | 38.9971 |
| exposure | 0.6080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
