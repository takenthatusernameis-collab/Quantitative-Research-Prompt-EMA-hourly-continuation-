# EMA Hourly Continuation — AXS/USDT P20_200

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0290 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -2.0040 |
| sortino_ratio | -0.5303 |
| max_drawdown | 0.5024 |
| cagr | -0.2242 |
| net_avg_win | 70.5852 |
| net_avg_loss | -96.7593 |
| avg_hold_time_bars | 39.9324 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
