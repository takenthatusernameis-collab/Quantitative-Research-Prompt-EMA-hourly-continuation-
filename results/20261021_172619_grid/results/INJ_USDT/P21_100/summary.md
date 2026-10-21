# EMA Hourly Continuation — INJ/USDT P21_100

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8129 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9796 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.5041 |
| sortino_ratio | -0.4675 |
| max_drawdown | 0.4470 |
| cagr | -0.1948 |
| net_avg_win | 78.2105 |
| net_avg_loss | -93.4112 |
| avg_hold_time_bars | 16.2537 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
