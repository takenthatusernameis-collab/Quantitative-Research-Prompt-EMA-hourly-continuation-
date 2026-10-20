# EMA Hourly Continuation — MTL/USDT P8_20

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.3576 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -12.1771 |
| sortino_ratio | -6.6544 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 9.0509 |
| net_avg_loss | -17.8692 |
| avg_hold_time_bars | 4.2550 |
| exposure | 0.2861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
