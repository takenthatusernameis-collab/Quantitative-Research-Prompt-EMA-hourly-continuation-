# EMA Hourly Continuation — XLM/USDT P8_200

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5645 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9408 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -3.1171 |
| sortino_ratio | -0.8665 |
| max_drawdown | 0.6730 |
| cagr | -0.3461 |
| net_avg_win | 44.5104 |
| net_avg_loss | -73.1104 |
| avg_hold_time_bars | 43.6725 |
| exposure | 0.7881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
