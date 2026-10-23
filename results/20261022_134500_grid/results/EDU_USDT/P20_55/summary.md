# EMA Hourly Continuation — EDU/USDT P20_55

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.4869 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7542 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -6.5717 |
| sortino_ratio | -2.9454 |
| max_drawdown | 0.9724 |
| cagr | -0.7538 |
| net_avg_win | 20.4756 |
| net_avg_loss | -33.7302 |
| avg_hold_time_bars | 5.5915 |
| exposure | 0.2558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
