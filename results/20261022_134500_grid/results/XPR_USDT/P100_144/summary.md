# EMA Hourly Continuation — XPR/USDT P100_144

**Symbol:** XPR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.3452 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7239 |
| gross_win_rate | 0.4312 |
| sharpe_ratio | -6.8625 |
| sortino_ratio | -2.1805 |
| max_drawdown | 0.9379 |
| cagr | -0.6660 |
| net_avg_win | 23.7334 |
| net_avg_loss | -49.9993 |
| avg_hold_time_bars | 4.2632 |
| exposure | 0.0957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
