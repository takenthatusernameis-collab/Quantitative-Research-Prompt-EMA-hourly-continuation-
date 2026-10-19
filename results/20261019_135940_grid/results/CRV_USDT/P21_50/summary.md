# EMA Hourly Continuation — CRV/USDT P21_50

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.5755 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -5.9083 |
| sortino_ratio | -2.6348 |
| max_drawdown | 0.9608 |
| cagr | -0.7213 |
| net_avg_win | 26.8773 |
| net_avg_loss | -43.8069 |
| avg_hold_time_bars | 3.8620 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
