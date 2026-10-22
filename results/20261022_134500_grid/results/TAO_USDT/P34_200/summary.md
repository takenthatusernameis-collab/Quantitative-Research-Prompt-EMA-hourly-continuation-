# EMA Hourly Continuation — TAO/USDT P34_200

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7552 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.7532 |
| sortino_ratio | -0.4900 |
| max_drawdown | 0.4637 |
| cagr | -0.2068 |
| net_avg_win | 69.7913 |
| net_avg_loss | -92.4127 |
| avg_hold_time_bars | 26.9179 |
| exposure | 0.4772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
