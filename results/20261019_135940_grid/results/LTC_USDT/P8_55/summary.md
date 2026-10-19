# EMA Hourly Continuation — LTC/USDT P8_55

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.3943 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -9.2208 |
| sortino_ratio | -4.2987 |
| max_drawdown | 0.9962 |
| cagr | -0.8906 |
| net_avg_win | 13.5391 |
| net_avg_loss | -26.0232 |
| avg_hold_time_bars | 8.9946 |
| exposure | 0.4542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
