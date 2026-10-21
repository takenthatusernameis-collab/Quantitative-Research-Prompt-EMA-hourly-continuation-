# EMA Hourly Continuation — XYO/USDT P21_26

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.4985 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.4263 |
| sharpe_ratio | -3.7212 |
| sortino_ratio | -0.8439 |
| max_drawdown | 0.6396 |
| cagr | -0.3249 |
| net_avg_win | 58.4070 |
| net_avg_loss | -87.0683 |
| avg_hold_time_bars | 5.6215 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
