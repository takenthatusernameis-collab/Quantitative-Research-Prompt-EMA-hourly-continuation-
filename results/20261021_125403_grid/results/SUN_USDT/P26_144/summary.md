# EMA Hourly Continuation — SUN/USDT P26_144

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.4832 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.7511 |
| gross_win_rate | 0.4206 |
| sharpe_ratio | -4.6791 |
| sortino_ratio | -1.2528 |
| max_drawdown | 0.7811 |
| cagr | -0.4514 |
| net_avg_win | 49.9508 |
| net_avg_loss | -70.8626 |
| avg_hold_time_bars | 29.1253 |
| exposure | 0.4732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
