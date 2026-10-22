# EMA Hourly Continuation — ZKJ/USDT P34_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.1561 |
| net_win_rate | 0.2720 |
| gross_profit_factor | 0.4656 |
| gross_win_rate | 0.3653 |
| sharpe_ratio | -9.8103 |
| sortino_ratio | -2.8856 |
| max_drawdown | 0.9810 |
| cagr | -0.7903 |
| net_avg_win | 17.7722 |
| net_avg_loss | -42.5454 |
| avg_hold_time_bars | 43.9040 |
| exposure | 0.7484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
