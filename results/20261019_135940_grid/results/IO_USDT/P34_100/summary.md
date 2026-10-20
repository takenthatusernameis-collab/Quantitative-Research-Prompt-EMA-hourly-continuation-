# EMA Hourly Continuation — IO/USDT P34_100

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.5851 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8495 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -4.4033 |
| sortino_ratio | -1.6223 |
| max_drawdown | 0.8449 |
| cagr | -0.5428 |
| net_avg_win | 39.5811 |
| net_avg_loss | -57.9854 |
| avg_hold_time_bars | 7.4077 |
| exposure | 0.2331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
