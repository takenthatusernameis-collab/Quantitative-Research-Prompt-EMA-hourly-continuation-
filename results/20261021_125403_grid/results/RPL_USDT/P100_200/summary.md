# EMA Hourly Continuation — RPL/USDT P100_200

**Symbol:** RPL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.7502 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.6483 |
| sortino_ratio | -0.4070 |
| max_drawdown | 0.3913 |
| cagr | -0.1713 |
| net_avg_win | 77.1162 |
| net_avg_loss | -98.7570 |
| avg_hold_time_bars | 11.4767 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
