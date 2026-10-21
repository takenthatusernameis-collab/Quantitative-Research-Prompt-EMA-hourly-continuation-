# EMA Hourly Continuation — TWT/USDT P21_89

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.7357 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0056 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -2.2812 |
| sortino_ratio | -0.7697 |
| max_drawdown | 0.6188 |
| cagr | -0.2980 |
| net_avg_win | 58.9543 |
| net_avg_loss | -80.7126 |
| avg_hold_time_bars | 13.8791 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
