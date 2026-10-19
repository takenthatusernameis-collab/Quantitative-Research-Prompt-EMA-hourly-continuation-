# EMA Hourly Continuation — BTT/USDT P34_200

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.4069 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -4.3673 |
| sortino_ratio | -1.0001 |
| max_drawdown | 0.7255 |
| cagr | -0.4016 |
| net_avg_win | 43.6174 |
| net_avg_loss | -77.8269 |
| avg_hold_time_bars | 47.9114 |
| exposure | 0.5902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
