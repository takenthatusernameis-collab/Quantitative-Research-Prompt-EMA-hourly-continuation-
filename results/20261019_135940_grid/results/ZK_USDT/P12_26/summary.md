# EMA Hourly Continuation — ZK/USDT P12_26

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1358 |
| net_profit_factor | 0.5668 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 1.0231 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -9.6901 |
| sortino_ratio | -5.1957 |
| max_drawdown | 0.9977 |
| cagr | -0.9248 |
| net_avg_win | 21.7948 |
| net_avg_loss | -30.3448 |
| avg_hold_time_bars | 2.9293 |
| exposure | 0.1939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
