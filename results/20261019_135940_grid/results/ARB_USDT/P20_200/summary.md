# EMA Hourly Continuation — ARB/USDT P20_200

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7898 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0633 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.2729 |
| sortino_ratio | -0.3086 |
| max_drawdown | 0.3256 |
| cagr | -0.1369 |
| net_avg_win | 77.4501 |
| net_avg_loss | -102.8579 |
| avg_hold_time_bars | 52.2969 |
| exposure | 0.6965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
