# EMA Hourly Continuation — ADA/USDT P8_50

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.9589 |
| sortino_ratio | -0.7227 |
| max_drawdown | 0.6432 |
| cagr | -0.2839 |
| net_avg_win | 56.0705 |
| net_avg_loss | -74.0060 |
| avg_hold_time_bars | 12.9758 |
| exposure | 0.3905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
