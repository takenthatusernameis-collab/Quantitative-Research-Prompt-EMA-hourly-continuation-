# EMA Hourly Continuation — CYBER/USDT P34_55

**Symbol:** CYBER/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.5970 |
| sortino_ratio | -0.7346 |
| max_drawdown | 0.5754 |
| cagr | -0.2865 |
| net_avg_win | 63.7311 |
| net_avg_loss | -89.1249 |
| avg_hold_time_bars | 6.9410 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
