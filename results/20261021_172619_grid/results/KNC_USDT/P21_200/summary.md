# EMA Hourly Continuation — KNC/USDT P21_200

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.9209 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1582 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.4157 |
| sortino_ratio | -0.1046 |
| max_drawdown | 0.2833 |
| cagr | -0.0502 |
| net_avg_win | 86.6551 |
| net_avg_loss | -109.5566 |
| avg_hold_time_bars | 48.8119 |
| exposure | 0.6723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
