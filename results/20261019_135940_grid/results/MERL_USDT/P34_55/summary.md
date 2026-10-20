# EMA Hourly Continuation — MERL/USDT P34_55

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4030 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.6413 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -7.0819 |
| sortino_ratio | -2.9865 |
| max_drawdown | 0.9724 |
| cagr | -0.7598 |
| net_avg_win | 17.5405 |
| net_avg_loss | -32.1086 |
| avg_hold_time_bars | 3.2077 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
