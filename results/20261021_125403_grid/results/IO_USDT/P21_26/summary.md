# EMA Hourly Continuation — IO/USDT P21_26

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 147 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -1.4516 |
| sortino_ratio | -0.2589 |
| max_drawdown | 0.3060 |
| cagr | -0.1123 |
| net_avg_win | 84.8650 |
| net_avg_loss | -106.4595 |
| avg_hold_time_bars | 4.8980 |
| exposure | 0.0349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
