# EMA Hourly Continuation — XRP/USDT P21_34

**Symbol:** XRP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1153 |
| net_profit_factor | 0.1728 |
| net_win_rate | 0.3469 |
| gross_profit_factor | 0.8106 |
| gross_win_rate | 0.4215 |
| sharpe_ratio | -15.0726 |
| sortino_ratio | -7.5276 |
| max_drawdown | 1.0000 |
| cagr | -0.9835 |
| net_avg_win | 5.2223 |
| net_avg_loss | -16.0539 |
| avg_hold_time_bars | 2.1535 |
| exposure | 0.1129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
