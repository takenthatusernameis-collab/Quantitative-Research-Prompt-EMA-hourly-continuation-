# EMA Hourly Continuation — ETN/USDT P55_100

**Symbol:** ETN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5094 |
| net_win_rate | 0.3969 |
| gross_profit_factor | 0.6528 |
| gross_win_rate | 0.3969 |
| sharpe_ratio | -3.6583 |
| sortino_ratio | -0.9053 |
| max_drawdown | 0.6025 |
| cagr | -0.3426 |
| net_avg_win | 59.6368 |
| net_avg_loss | -77.0391 |
| avg_hold_time_bars | 8.3852 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
