# EMA Hourly Continuation — REZ/USDT P26_144

**Symbol:** REZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8622 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.1250 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -1.1025 |
| sortino_ratio | -0.3520 |
| max_drawdown | 0.4378 |
| cagr | -0.1539 |
| net_avg_win | 82.1419 |
| net_avg_loss | -106.4070 |
| avg_hold_time_bars | 21.7771 |
| exposure | 0.4913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
