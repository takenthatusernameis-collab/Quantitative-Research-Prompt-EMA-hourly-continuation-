# EMA Hourly Continuation — DODO/USDT P20_55

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.5586 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -7.7174 |
| sortino_ratio | -3.4355 |
| max_drawdown | 0.9869 |
| cagr | -0.8168 |
| net_avg_win | 28.6271 |
| net_avg_loss | -38.6561 |
| avg_hold_time_bars | 5.8886 |
| exposure | 0.2702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
