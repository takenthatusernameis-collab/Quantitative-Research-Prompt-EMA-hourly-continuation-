# EMA Hourly Continuation — SSV/USDT P50_100

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7032 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.2321 |
| sortino_ratio | -0.6515 |
| max_drawdown | 0.5542 |
| cagr | -0.2577 |
| net_avg_win | 61.9999 |
| net_avg_loss | -81.6940 |
| avg_hold_time_bars | 8.2524 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
