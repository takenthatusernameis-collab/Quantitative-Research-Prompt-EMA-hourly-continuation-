# EMA Hourly Continuation — LTC/USDT P12_100

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.4665 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -6.0198 |
| sortino_ratio | -2.1604 |
| max_drawdown | 0.9368 |
| cagr | -0.6603 |
| net_avg_win | 27.4896 |
| net_avg_loss | -48.4758 |
| avg_hold_time_bars | 18.5912 |
| exposure | 0.5560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
