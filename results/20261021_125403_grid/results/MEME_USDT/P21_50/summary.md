# EMA Hourly Continuation — MEME/USDT P21_50

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6650 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -3.2447 |
| sortino_ratio | -1.0921 |
| max_drawdown | 0.7361 |
| cagr | -0.3936 |
| net_avg_win | 54.8312 |
| net_avg_loss | -71.6578 |
| avg_hold_time_bars | 6.4704 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
