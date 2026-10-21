# EMA Hourly Continuation — SHIB/USDT P34_100

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7472 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -1.9997 |
| sortino_ratio | -0.5889 |
| max_drawdown | 0.5145 |
| cagr | -0.2367 |
| net_avg_win | 69.3148 |
| net_avg_loss | -91.8907 |
| avg_hold_time_bars | 12.8863 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
