# EMA Hourly Continuation — LDO/USDT P34_89

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.2424 |
| sortino_ratio | -0.6611 |
| max_drawdown | 0.5418 |
| cagr | -0.2621 |
| net_avg_win | 64.4475 |
| net_avg_loss | -80.2334 |
| avg_hold_time_bars | 11.6620 |
| exposure | 0.2274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
