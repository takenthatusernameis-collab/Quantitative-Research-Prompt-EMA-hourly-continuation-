# EMA Hourly Continuation — LDO/USDT P12_20

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7436 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.5231 |
| sortino_ratio | -0.3789 |
| max_drawdown | 0.3642 |
| cagr | -0.1593 |
| net_avg_win | 67.4111 |
| net_avg_loss | -93.7347 |
| avg_hold_time_bars | 4.0870 |
| exposure | 0.0555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
