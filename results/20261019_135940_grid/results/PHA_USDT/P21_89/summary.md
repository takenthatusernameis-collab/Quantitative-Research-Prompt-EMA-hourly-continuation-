# EMA Hourly Continuation — PHA/USDT P21_89

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8333 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -4.3145 |
| sortino_ratio | -1.6314 |
| max_drawdown | 0.8626 |
| cagr | -0.5421 |
| net_avg_win | 32.8594 |
| net_avg_loss | -50.3496 |
| avg_hold_time_bars | 11.3370 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
