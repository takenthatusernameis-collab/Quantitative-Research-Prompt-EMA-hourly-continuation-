# EMA Hourly Continuation — EDU/USDT P20_50

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.7359 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -7.1201 |
| sortino_ratio | -3.2425 |
| max_drawdown | 0.9815 |
| cagr | -0.7888 |
| net_avg_win | 17.3129 |
| net_avg_loss | -30.4286 |
| avg_hold_time_bars | 4.9924 |
| exposure | 0.2365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
