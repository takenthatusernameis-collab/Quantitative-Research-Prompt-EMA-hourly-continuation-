# EMA Hourly Continuation — SNX/USDT P34_50

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.4260 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -8.1913 |
| sortino_ratio | -3.5230 |
| max_drawdown | 0.9884 |
| cagr | -0.8281 |
| net_avg_win | 17.5076 |
| net_avg_loss | -34.1625 |
| avg_hold_time_bars | 2.7064 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
