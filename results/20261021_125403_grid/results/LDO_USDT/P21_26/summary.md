# EMA Hourly Continuation — LDO/USDT P21_26

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.7447 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.0981 |
| sortino_ratio | -0.2041 |
| max_drawdown | 0.2501 |
| cagr | -0.0893 |
| net_avg_win | 71.8604 |
| net_avg_loss | -100.0213 |
| avg_hold_time_bars | 4.4611 |
| exposure | 0.0339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
