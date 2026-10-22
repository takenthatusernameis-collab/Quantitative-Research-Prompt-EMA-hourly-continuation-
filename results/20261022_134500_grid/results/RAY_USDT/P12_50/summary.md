# EMA Hourly Continuation — RAY/USDT P12_50

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.6286 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -5.7733 |
| sortino_ratio | -2.6473 |
| max_drawdown | 0.9622 |
| cagr | -0.7179 |
| net_avg_win | 33.1046 |
| net_avg_loss | -45.2711 |
| avg_hold_time_bars | 6.8623 |
| exposure | 0.3306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
