# EMA Hourly Continuation — ORCA/USDT P34_50

**Symbol:** ORCA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6603 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.7073 |
| sortino_ratio | -0.7448 |
| max_drawdown | 0.5923 |
| cagr | -0.2908 |
| net_avg_win | 62.4121 |
| net_avg_loss | -90.0245 |
| avg_hold_time_bars | 6.2927 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
