# EMA Hourly Continuation — ONT/USDT P8_50

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -7.5486 |
| sortino_ratio | -3.5750 |
| max_drawdown | 0.9886 |
| cagr | -0.8271 |
| net_avg_win | 27.5167 |
| net_avg_loss | -36.5222 |
| avg_hold_time_bars | 8.4639 |
| exposure | 0.4401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
