# EMA Hourly Continuation — ETC/USDT P55_89

**Symbol:** ETC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6667 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0245 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -2.0065 |
| sortino_ratio | -0.5040 |
| max_drawdown | 0.4551 |
| cagr | -0.2051 |
| net_avg_win | 56.1759 |
| net_avg_loss | -89.4195 |
| avg_hold_time_bars | 6.7162 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
