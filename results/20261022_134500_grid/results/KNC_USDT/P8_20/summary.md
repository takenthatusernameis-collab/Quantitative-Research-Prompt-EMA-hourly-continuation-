# EMA Hourly Continuation — KNC/USDT P8_20

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1478 |
| net_profit_factor | 0.3229 |
| net_win_rate | 0.4032 |
| gross_profit_factor | 0.7705 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -12.6863 |
| sortino_ratio | -6.9321 |
| max_drawdown | 0.9999 |
| cagr | -0.9699 |
| net_avg_win | 8.0009 |
| net_avg_loss | -16.7427 |
| avg_hold_time_bars | 3.9668 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
