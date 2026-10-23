# EMA Hourly Continuation — WAVES/USDT P26_100

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8674 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -6.6237 |
| sortino_ratio | -2.6178 |
| max_drawdown | 0.9625 |
| cagr | -0.7244 |
| net_avg_win | 29.8118 |
| net_avg_loss | -44.0373 |
| avg_hold_time_bars | 9.5722 |
| exposure | 0.3437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
