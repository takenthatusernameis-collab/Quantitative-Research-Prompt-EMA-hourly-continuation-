# EMA Hourly Continuation — XTZ/USDT P21_34

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1201 |
| net_profit_factor | 0.2969 |
| net_win_rate | 0.3972 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -12.3561 |
| sortino_ratio | -6.1391 |
| max_drawdown | 0.9996 |
| cagr | -0.9575 |
| net_avg_win | 8.8490 |
| net_avg_loss | -19.6373 |
| avg_hold_time_bars | 2.7977 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
