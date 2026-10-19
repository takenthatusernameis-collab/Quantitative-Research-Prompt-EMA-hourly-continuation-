# EMA Hourly Continuation — JASMY/USDT P21_55

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.5270 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8819 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -6.3177 |
| sortino_ratio | -2.7725 |
| max_drawdown | 0.9665 |
| cagr | -0.7404 |
| net_avg_win | 23.7672 |
| net_avg_loss | -39.2851 |
| avg_hold_time_bars | 4.4913 |
| exposure | 0.1986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
