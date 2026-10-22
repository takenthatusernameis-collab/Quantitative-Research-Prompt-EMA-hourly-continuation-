# EMA Hourly Continuation — LQTY/USDT P8_20

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -3.9391 |
| sortino_ratio | -1.5019 |
| max_drawdown | 0.8323 |
| cagr | -0.4978 |
| net_avg_win | 43.6178 |
| net_avg_loss | -59.7077 |
| avg_hold_time_bars | 5.5182 |
| exposure | 0.1788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
