# EMA Hourly Continuation — AR/USDT P21_34

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.3603 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.6864 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -10.6627 |
| sortino_ratio | -5.1270 |
| max_drawdown | 0.9985 |
| cagr | -0.9246 |
| net_avg_win | 12.1205 |
| net_avg_loss | -22.7533 |
| avg_hold_time_bars | 2.5687 |
| exposure | 0.1343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
