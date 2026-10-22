# EMA Hourly Continuation — AXS/USDT P8_26

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.7085 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -9.9781 |
| sortino_ratio | -5.4488 |
| max_drawdown | 0.9989 |
| cagr | -0.9328 |
| net_avg_win | 7.5944 |
| net_avg_loss | -18.1181 |
| avg_hold_time_bars | 3.9223 |
| exposure | 0.2671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
