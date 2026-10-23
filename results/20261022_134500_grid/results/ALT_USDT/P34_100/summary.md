# EMA Hourly Continuation — ALT/USDT P34_100

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.6549 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -3.1757 |
| sortino_ratio | -1.0937 |
| max_drawdown | 0.7322 |
| cagr | -0.4020 |
| net_avg_win | 48.4411 |
| net_avg_loss | -67.9855 |
| avg_hold_time_bars | 11.7352 |
| exposure | 0.3163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
