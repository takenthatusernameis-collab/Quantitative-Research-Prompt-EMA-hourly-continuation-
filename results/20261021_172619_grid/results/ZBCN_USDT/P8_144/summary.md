# EMA Hourly Continuation — ZBCN/USDT P8_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 1.0098 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1504 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | 0.1513 |
| sortino_ratio | 0.0493 |
| max_drawdown | 0.2926 |
| cagr | 0.0115 |
| net_avg_win | 109.3966 |
| net_avg_loss | -126.7052 |
| avg_hold_time_bars | 28.5170 |
| exposure | 0.6584 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
