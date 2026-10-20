# EMA Hourly Continuation — IO/USDT P100_200

**Symbol:** IO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -3.0520 |
| sortino_ratio | -0.8711 |
| max_drawdown | 0.6503 |
| cagr | -0.3493 |
| net_avg_win | 58.7812 |
| net_avg_loss | -85.4201 |
| avg_hold_time_bars | 9.8791 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
