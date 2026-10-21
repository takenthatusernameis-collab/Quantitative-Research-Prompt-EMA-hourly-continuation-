# EMA Hourly Continuation — NEO/USDT P21_55

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.5916 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.9406 |
| sortino_ratio | -1.3121 |
| max_drawdown | 0.7819 |
| cagr | -0.4519 |
| net_avg_win | 45.8833 |
| net_avg_loss | -64.0227 |
| avg_hold_time_bars | 8.5239 |
| exposure | 0.2108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
