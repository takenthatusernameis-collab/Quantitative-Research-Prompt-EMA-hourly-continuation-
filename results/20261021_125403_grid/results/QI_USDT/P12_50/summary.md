# EMA Hourly Continuation — QI/USDT P12_50

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6847 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9150 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.0674 |
| sortino_ratio | -1.1530 |
| max_drawdown | 0.7414 |
| cagr | -0.4102 |
| net_avg_win | 47.6973 |
| net_avg_loss | -64.8284 |
| avg_hold_time_bars | 10.5122 |
| exposure | 0.3306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
