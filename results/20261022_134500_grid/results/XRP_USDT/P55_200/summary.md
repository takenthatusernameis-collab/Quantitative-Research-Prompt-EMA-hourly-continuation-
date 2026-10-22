# EMA Hourly Continuation — XRP/USDT P55_200

**Symbol:** XRP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.3978 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.7829 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -4.9764 |
| sortino_ratio | -1.4362 |
| max_drawdown | 0.8441 |
| cagr | -0.5150 |
| net_avg_win | 29.5903 |
| net_avg_loss | -58.1948 |
| avg_hold_time_bars | 17.1080 |
| exposure | 0.3313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
