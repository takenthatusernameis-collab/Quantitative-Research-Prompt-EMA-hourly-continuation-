# EMA Hourly Continuation — ONT/USDT P26_89

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.9650 |
| sortino_ratio | -0.6084 |
| max_drawdown | 0.5648 |
| cagr | -0.2443 |
| net_avg_win | 67.5373 |
| net_avg_loss | -86.7591 |
| avg_hold_time_bars | 14.6178 |
| exposure | 0.3116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
