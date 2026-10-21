# EMA Hourly Continuation — XMR/USDT P26_89

**Symbol:** XMR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -2.9242 |
| sortino_ratio | -0.8863 |
| max_drawdown | 0.6528 |
| cagr | -0.3339 |
| net_avg_win | 58.2603 |
| net_avg_loss | -76.1121 |
| avg_hold_time_bars | 11.1435 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
