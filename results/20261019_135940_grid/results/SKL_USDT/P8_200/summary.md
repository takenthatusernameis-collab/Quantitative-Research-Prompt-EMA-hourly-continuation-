# EMA Hourly Continuation — SKL/USDT P8_200

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.5754 |
| sortino_ratio | -0.7609 |
| max_drawdown | 0.6498 |
| cagr | -0.3010 |
| net_avg_win | 61.9637 |
| net_avg_loss | -82.4546 |
| avg_hold_time_bars | 39.5708 |
| exposure | 0.7878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
