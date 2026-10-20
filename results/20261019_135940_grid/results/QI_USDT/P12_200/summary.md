# EMA Hourly Continuation — QI/USDT P12_200

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5938 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8531 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.4426 |
| sortino_ratio | -0.9842 |
| max_drawdown | 0.7015 |
| cagr | -0.3715 |
| net_avg_win | 55.4380 |
| net_avg_loss | -72.9244 |
| avg_hold_time_bars | 36.9108 |
| exposure | 0.6932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
