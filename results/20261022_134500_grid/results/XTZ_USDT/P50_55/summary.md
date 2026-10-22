# EMA Hourly Continuation — XTZ/USDT P50_55

**Symbol:** XTZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.1921 |
| net_win_rate | 0.3399 |
| gross_profit_factor | 0.8594 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -13.6351 |
| sortino_ratio | -6.1284 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 7.6938 |
| net_avg_loss | -20.6246 |
| avg_hold_time_bars | 1.9175 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
