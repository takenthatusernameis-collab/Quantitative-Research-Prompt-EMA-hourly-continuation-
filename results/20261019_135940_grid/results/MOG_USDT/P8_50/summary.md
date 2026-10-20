# EMA Hourly Continuation — MOG/USDT P8_50

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.1663 |
| sortino_ratio | -1.9037 |
| max_drawdown | 0.8758 |
| cagr | -0.5942 |
| net_avg_win | 45.8078 |
| net_avg_loss | -59.7407 |
| avg_hold_time_bars | 9.9406 |
| exposure | 0.4739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
