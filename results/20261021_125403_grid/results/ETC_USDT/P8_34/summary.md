# EMA Hourly Continuation — ETC/USDT P8_34

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -3.8261 |
| sortino_ratio | -1.4873 |
| max_drawdown | 0.8227 |
| cagr | -0.4930 |
| net_avg_win | 43.2461 |
| net_avg_loss | -61.7748 |
| avg_hold_time_bars | 8.6875 |
| exposure | 0.2906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
