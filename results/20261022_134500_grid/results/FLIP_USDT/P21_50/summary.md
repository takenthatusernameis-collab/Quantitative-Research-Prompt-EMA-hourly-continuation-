# EMA Hourly Continuation — FLIP/USDT P21_50

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.3958 |
| net_win_rate | 0.3956 |
| gross_profit_factor | 0.7741 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -8.1539 |
| sortino_ratio | -3.0030 |
| max_drawdown | 0.9801 |
| cagr | -0.7876 |
| net_avg_win | 23.6785 |
| net_avg_loss | -39.1606 |
| avg_hold_time_bars | 8.4175 |
| exposure | 0.2621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
