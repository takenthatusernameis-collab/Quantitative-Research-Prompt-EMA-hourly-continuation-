# EMA Hourly Continuation — PHA/USDT P20_26

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.2789 |
| net_win_rate | 0.4005 |
| gross_profit_factor | 0.7616 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -12.0583 |
| sortino_ratio | -6.0104 |
| max_drawdown | 0.9996 |
| cagr | -0.9562 |
| net_avg_win | 7.8745 |
| net_avg_loss | -18.8605 |
| avg_hold_time_bars | 2.0865 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
