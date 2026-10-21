# EMA Hourly Continuation — UNI/USDT P12_200

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.4139 |
| sortino_ratio | -0.3428 |
| max_drawdown | 0.3358 |
| cagr | -0.1469 |
| net_avg_win | 76.5953 |
| net_avg_loss | -89.9992 |
| avg_hold_time_bars | 52.9247 |
| exposure | 0.7025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
