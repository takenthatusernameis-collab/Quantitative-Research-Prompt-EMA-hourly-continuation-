# EMA Hourly Continuation — RSR/USDT P20_21

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.8434 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1178 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.5828 |
| sortino_ratio | -0.0968 |
| max_drawdown | 0.1671 |
| cagr | -0.0440 |
| net_avg_win | 82.2341 |
| net_avg_loss | -110.0857 |
| avg_hold_time_bars | 5.1818 |
| exposure | 0.0311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
