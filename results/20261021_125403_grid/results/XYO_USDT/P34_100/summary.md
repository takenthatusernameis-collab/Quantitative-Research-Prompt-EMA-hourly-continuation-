# EMA Hourly Continuation — XYO/USDT P34_100

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6021 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8141 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -3.4083 |
| sortino_ratio | -0.9623 |
| max_drawdown | 0.6872 |
| cagr | -0.3594 |
| net_avg_win | 58.6778 |
| net_avg_loss | -76.3876 |
| avg_hold_time_bars | 14.4823 |
| exposure | 0.2595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
