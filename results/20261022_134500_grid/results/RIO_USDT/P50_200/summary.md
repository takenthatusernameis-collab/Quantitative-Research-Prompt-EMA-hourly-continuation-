# EMA Hourly Continuation — RIO/USDT P50_200

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6214 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -3.3744 |
| sortino_ratio | -1.0560 |
| max_drawdown | 0.7415 |
| cagr | -0.3946 |
| net_avg_win | 52.9422 |
| net_avg_loss | -69.9953 |
| avg_hold_time_bars | 15.2612 |
| exposure | 0.3433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
