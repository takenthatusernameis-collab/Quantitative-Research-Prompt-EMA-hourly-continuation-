# EMA Hourly Continuation — KSM/USDT P21_50

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.4685 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -7.9888 |
| sortino_ratio | -3.5440 |
| max_drawdown | 0.9871 |
| cagr | -0.8206 |
| net_avg_win | 20.5559 |
| net_avg_loss | -33.5651 |
| avg_hold_time_bars | 5.0820 |
| exposure | 0.2255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
