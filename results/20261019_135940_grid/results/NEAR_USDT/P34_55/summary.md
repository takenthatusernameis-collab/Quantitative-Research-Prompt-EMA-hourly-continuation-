# EMA Hourly Continuation — NEAR/USDT P34_55

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 882 |
| net_profit_factor | 0.4506 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4546 |
| sharpe_ratio | -7.5579 |
| sortino_ratio | -3.1638 |
| max_drawdown | 0.9811 |
| cagr | -0.7933 |
| net_avg_win | 20.3189 |
| net_avg_loss | -36.7398 |
| avg_hold_time_bars | 2.9671 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
