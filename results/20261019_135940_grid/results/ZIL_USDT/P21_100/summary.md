# EMA Hourly Continuation — ZIL/USDT P21_100

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6101 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -4.5041 |
| sortino_ratio | -1.6601 |
| max_drawdown | 0.8752 |
| cagr | -0.5499 |
| net_avg_win | 41.6533 |
| net_avg_loss | -61.9844 |
| avg_hold_time_bars | 12.8082 |
| exposure | 0.3976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
