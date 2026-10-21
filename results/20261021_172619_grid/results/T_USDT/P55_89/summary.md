# EMA Hourly Continuation — T/USDT P55_89

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.5412 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8309 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -3.7348 |
| sortino_ratio | -1.0594 |
| max_drawdown | 0.7178 |
| cagr | -0.3844 |
| net_avg_win | 46.2656 |
| net_avg_loss | -71.9025 |
| avg_hold_time_bars | 9.1904 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
