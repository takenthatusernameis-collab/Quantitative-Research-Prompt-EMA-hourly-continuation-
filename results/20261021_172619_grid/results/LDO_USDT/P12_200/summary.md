# EMA Hourly Continuation — LDO/USDT P12_200

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.7396 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -1.3498 |
| sortino_ratio | -0.2912 |
| max_drawdown | 0.3412 |
| cagr | -0.1263 |
| net_avg_win | 75.6072 |
| net_avg_loss | -89.0351 |
| avg_hold_time_bars | 73.6078 |
| exposure | 0.7762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
