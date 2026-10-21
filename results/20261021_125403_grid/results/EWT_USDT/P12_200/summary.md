# EMA Hourly Continuation — EWT/USDT P12_200

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7108 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -1.9922 |
| sortino_ratio | -0.5526 |
| max_drawdown | 0.5428 |
| cagr | -0.2251 |
| net_avg_win | 66.0421 |
| net_avg_loss | -78.9952 |
| avg_hold_time_bars | 33.9164 |
| exposure | 0.5905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
