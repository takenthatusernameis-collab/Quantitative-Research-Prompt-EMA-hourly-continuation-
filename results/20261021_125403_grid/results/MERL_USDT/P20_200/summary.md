# EMA Hourly Continuation — MERL/USDT P20_200

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7584 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8728 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -1.7721 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4838 |
| cagr | -0.1887 |
| net_avg_win | 86.4477 |
| net_avg_loss | -95.8551 |
| avg_hold_time_bars | 41.6944 |
| exposure | 0.6158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
