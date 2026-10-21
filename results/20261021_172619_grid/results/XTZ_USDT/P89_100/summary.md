# EMA Hourly Continuation — XTZ/USDT P89_100

**Symbol:** XTZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 133 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.8347 |
| sortino_ratio | -0.3050 |
| max_drawdown | 0.3017 |
| cagr | -0.1297 |
| net_avg_win | 62.9567 |
| net_avg_loss | -103.4848 |
| avg_hold_time_bars | 4.6617 |
| exposure | 0.0282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
