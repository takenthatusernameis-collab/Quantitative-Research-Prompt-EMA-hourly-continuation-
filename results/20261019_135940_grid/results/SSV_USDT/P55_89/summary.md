# EMA Hourly Continuation — SSV/USDT P55_89

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.4484 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.8217 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -6.7664 |
| sortino_ratio | -2.6039 |
| max_drawdown | 0.9635 |
| cagr | -0.7224 |
| net_avg_win | 24.0295 |
| net_avg_loss | -40.8803 |
| avg_hold_time_bars | 4.0945 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
