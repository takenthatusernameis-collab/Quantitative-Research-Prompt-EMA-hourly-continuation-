# EMA Hourly Continuation — LDO/USDT P20_200

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8234 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.5051 |
| sortino_ratio | -0.6549 |
| max_drawdown | 0.5600 |
| cagr | -0.2668 |
| net_avg_win | 60.1728 |
| net_avg_loss | -79.2605 |
| avg_hold_time_bars | 40.8937 |
| exposure | 0.6469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
