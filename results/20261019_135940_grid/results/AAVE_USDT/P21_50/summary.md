# EMA Hourly Continuation — AAVE/USDT P21_50

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 996 |
| net_profit_factor | 0.4731 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8696 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -8.0884 |
| sortino_ratio | -3.5990 |
| max_drawdown | 0.9889 |
| cagr | -0.8306 |
| net_avg_win | 20.4522 |
| net_avg_loss | -33.3817 |
| avg_hold_time_bars | 4.4829 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
