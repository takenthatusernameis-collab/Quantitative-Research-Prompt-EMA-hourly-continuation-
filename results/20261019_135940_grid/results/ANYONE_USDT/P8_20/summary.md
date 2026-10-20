# EMA Hourly Continuation — ANYONE/USDT P8_20

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1453 |
| net_profit_factor | 0.4815 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.7775 |
| gross_win_rate | 0.4418 |
| sharpe_ratio | -9.1456 |
| sortino_ratio | -5.1613 |
| max_drawdown | 0.9966 |
| cagr | -0.9188 |
| net_avg_win | 14.6654 |
| net_avg_loss | -23.3813 |
| avg_hold_time_bars | 3.3957 |
| exposure | 0.2493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
