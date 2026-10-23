# EMA Hourly Continuation — GTC/USDT P8_34

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1210 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -7.6174 |
| sortino_ratio | -3.7319 |
| max_drawdown | 0.9893 |
| cagr | -0.8339 |
| net_avg_win | 19.1798 |
| net_avg_loss | -29.6364 |
| avg_hold_time_bars | 6.3000 |
| exposure | 0.3465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
