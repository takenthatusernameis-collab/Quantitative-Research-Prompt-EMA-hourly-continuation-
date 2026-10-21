# EMA Hourly Continuation — BIGTIME/USDT P8_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7926 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.6730 |
| sortino_ratio | -0.5219 |
| max_drawdown | 0.4865 |
| cagr | -0.2149 |
| net_avg_win | 74.9502 |
| net_avg_loss | -88.8396 |
| avg_hold_time_bars | 30.1559 |
| exposure | 0.6564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
