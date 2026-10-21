# EMA Hourly Continuation — ORCA/USDT P20_21

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.7003 |
| net_win_rate | 0.5221 |
| gross_profit_factor | 1.1340 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -1.6958 |
| sortino_ratio | -0.3681 |
| max_drawdown | 0.3884 |
| cagr | -0.1544 |
| net_avg_win | 68.0609 |
| net_avg_loss | -106.1850 |
| avg_hold_time_bars | 5.1947 |
| exposure | 0.0534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
