# EMA Hourly Continuation — QI/USDT P21_144

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9631 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.6666 |
| sortino_ratio | -0.4653 |
| max_drawdown | 0.4441 |
| cagr | -0.1931 |
| net_avg_win | 73.2415 |
| net_avg_loss | -90.7382 |
| avg_hold_time_bars | 29.1068 |
| exposure | 0.5058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
