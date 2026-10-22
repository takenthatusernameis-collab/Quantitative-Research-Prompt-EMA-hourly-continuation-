# EMA Hourly Continuation — AXS/USDT P20_55

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -5.5858 |
| sortino_ratio | -2.3093 |
| max_drawdown | 0.9426 |
| cagr | -0.6725 |
| net_avg_win | 29.7172 |
| net_avg_loss | -47.5714 |
| avg_hold_time_bars | 6.0323 |
| exposure | 0.2367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
