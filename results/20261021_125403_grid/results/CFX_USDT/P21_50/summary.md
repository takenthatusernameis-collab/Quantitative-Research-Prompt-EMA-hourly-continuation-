# EMA Hourly Continuation — CFX/USDT P21_50

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8035 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -3.3891 |
| sortino_ratio | -1.0523 |
| max_drawdown | 0.7270 |
| cagr | -0.3833 |
| net_avg_win | 49.6598 |
| net_avg_loss | -67.6496 |
| avg_hold_time_bars | 7.4863 |
| exposure | 0.1616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
